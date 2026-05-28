"""Vistas principales de la aplicación SGPR.
Funciones para el registro de permisos, reposos, trabajadores y auditoría.
"""

from io import BytesIO

from django.contrib import messages
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles import finders
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from openpyxl import Workbook
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from .forms import (
    CedulaAuthenticationForm,
    EliminarTrabajadorForm,
    EvaluacionSolicitudForm,
    RegistroTrabajadorForm,
    SolicitudForm,
    TrabajadorEditForm,
)
from .models import Auditoria, Solicitud, Trabajador


def get_encabezado_path():
    """Retorna la ruta absoluta del encabezado PNG si existe."""
    image_path = finders.find('images/encabezado.png') or finders.find('encabezado.png')
    return image_path


def es_gestion_humana(user):
    """Determina si el usuario pertenece a Gestión Humana (staff o grupo)."""
    return user.is_staff or user.groups.filter(name='Gestion_Humana').exists()


@login_required
def dashboard(request):
    """Panel principal: lista de solicitudes según el rol del usuario."""
    query = request.GET.get('q', '').strip()
    filtro_estado = request.GET.get('estado', 'TODOS')
    if es_gestion_humana(request.user):
        solicitudes = Solicitud.objects.select_related('trabajador__user').all().order_by('-fecha_creacion')
    else:
        solicitudes = Solicitud.objects.select_related('trabajador__user').filter(trabajador__user=request.user).order_by('-fecha_creacion')

    if filtro_estado and filtro_estado != 'TODOS':
        solicitudes = solicitudes.filter(estado=filtro_estado)

    if query:
        solicitudes = solicitudes.filter(
            Q(trabajador__cedula__icontains=query)
            | Q(trabajador__user__first_name__icontains=query)
            | Q(trabajador__user__last_name__icontains=query)
            | Q(trabajador__departamento__icontains=query)
            | Q(tipo__icontains=query)
            | Q(observaciones_admin__icontains=query)
        )

    # Paginación: 10 solicitudes por página
    page = request.GET.get('page', 1)
    paginator = Paginator(solicitudes, 10)
    try:
        solicitudes_page = paginator.page(page)
    except PageNotAnInteger:
        solicitudes_page = paginator.page(1)
    except EmptyPage:
        solicitudes_page = paginator.page(paginator.num_pages)

    return render(
        request,
        'dashboard.html',
        {
            'solicitudes': solicitudes_page,
            'page_obj': solicitudes_page,
            'paginator': paginator,
            'es_admin': es_gestion_humana(request.user),
            'query': query,
            'filtro_estado': filtro_estado,
            'estado_options': [
                ('TODOS', 'Todos'),
                ('PENDIENTE', 'Pendientes'),
                ('APROBADO', 'Aprobadas'),
                ('RECHAZO', 'Rechazadas'),
            ],
        },
    )


def registro_trabajador(request):
    """Permite el registro de nuevos trabajadores desde la página pública o desde un administrador autenticado."""
    if request.user.is_authenticated and not es_gestion_humana(request.user):
        return redirect('dashboard')

    from_admin = request.user.is_authenticated and es_gestion_humana(request.user)
    if request.method == 'POST':
        form = RegistroTrabajadorForm(request.POST)
        if form.is_valid():
            cedula = form.cleaned_data['cedula']
            nombres = form.cleaned_data['nombres']
            apellidos = form.cleaned_data['apellidos']
            cargo = form.cleaned_data['cargo']
            departamento = form.cleaned_data['departamento']
            # Use default password and require change at first login
            password = settings.DEFAULT_PASSWORD
            email = form.cleaned_data.get('email')

            username = cedula
            user = User.objects.create_user(
                username=username,
                first_name=nombres,
                last_name=apellidos,
                password=password,
            )
            if email:
                user.email = email
                user.save()

            trabajador = Trabajador.objects.create(
                user=user,
                cedula=cedula,
                cargo=cargo,
                departamento=departamento,
                password_reset_required=True,
            )

            Auditoria.objects.create(
                usuario=user,
                accion='REGISTRO',
                tabla_afectada='Trabajador',
                registro_id=trabajador.id,
                detalles=(
                    f"Registro de trabajador {trabajador.user.get_full_name()} (Cédula: {trabajador.cedula}) "
                    f"con usuario {user.username}."
                ),
            )

            messages.success(request, 'Trabajador registrado correctamente. Inicia sesión con la contraseña por defecto y cámbiala en tu primer acceso.')
            return render(
                request,
                'registro_exitoso.html',
                {
                    'username': username,
                    'password': settings.DEFAULT_PASSWORD,
                    'from_admin': request.user.is_authenticated and es_gestion_humana(request.user),
                },
            )
    else:
        form = RegistroTrabajadorForm()

    return render(request, 'registro_trabajador.html', {'form': form, 'from_admin': from_admin})


@csrf_exempt
@require_POST
def api_registro_trabajador(request):
    """API para registrar un nuevo trabajador sin enviar notificaciones por correo."""
    try:
        payload = json.loads(request.body.decode('utf-8') or '{}')
    except json.JSONDecodeError:
        payload = request.POST

    cedula = payload.get('cedula') or request.POST.get('cedula')
    nombres = payload.get('nombres') or request.POST.get('nombres')
    apellidos = payload.get('apellidos') or request.POST.get('apellidos')
    cargo = payload.get('cargo') or request.POST.get('cargo')
    departamento = payload.get('departamento') or request.POST.get('departamento')
    email = payload.get('email') or request.POST.get('email')

    if not all([cedula, nombres, apellidos, cargo, departamento]):
        return JsonResponse(
            {
                'success': False,
                'error': 'Faltan datos obligatorios. Se requieren cedula, nombres, apellidos, cargo y departamento.',
            },
            status=400,
        )

    if not cedula.isdigit():
        return JsonResponse(
            {
                'success': False,
                'error': 'La cédula solo debe contener números, sin letras ni caracteres especiales.',
            },
            status=400,
        )

    if Trabajador.objects.filter(cedula=cedula).exists() or User.objects.filter(username=cedula).exists():
        return JsonResponse(
            {'success': False, 'error': 'Ya existe un trabajador con esa cédula o usuario.'},
            status=400,
        )

    if email and User.objects.filter(email__iexact=email).exists():
        return JsonResponse(
            {'success': False, 'error': 'Ya existe un usuario registrado con este correo electrónico.'},
            status=400,
        )

    username = cedula
    password = settings.DEFAULT_PASSWORD
    user = User.objects.create_user(
        username=username,
        first_name=nombres,
        last_name=apellidos,
        password=password,
        email=email or '',
    )

    trabajador = Trabajador.objects.create(
        user=user,
        cedula=cedula,
        cargo=cargo,
        departamento=departamento,
        password_reset_required=True,
    )

    Auditoria.objects.create(
        usuario=user,
        accion='REGISTRO',
        tabla_afectada='Trabajador',
        registro_id=trabajador.id,
        detalles=(
            f"Registro de trabajador {trabajador.user.get_full_name()} (Cédula: {trabajador.cedula}) "
            f"con usuario {user.username} mediante API."
        ),
    )

    return JsonResponse(
        {
            'success': True,
            'message': 'Trabajador registrado correctamente.',
            'username': username,
        }
    )


@login_required
@user_passes_test(es_gestion_humana)
def lista_trabajadores(request):
    """Listado de trabajadores para Gestión Humana."""
    query = request.GET.get('q', '').strip()
    filtro_estado = request.GET.get('estado', 'TODOS')
    trabajadores = Trabajador.objects.select_related('user').all().order_by('user__last_name')

    if filtro_estado == 'OBLIGATORIO':
        trabajadores = trabajadores.filter(password_reset_required=True)
    elif filtro_estado == 'COMPLETO':
        trabajadores = trabajadores.filter(password_reset_required=False)

    if query:
        trabajadores = trabajadores.filter(
            Q(cedula__icontains=query)
            | Q(user__first_name__icontains=query)
            | Q(user__last_name__icontains=query)
            | Q(user__email__icontains=query)
            | Q(cargo__icontains=query)
            | Q(departamento__icontains=query)
        )

    # Paginación: 10 trabajadores por página
    page = request.GET.get('page', 1)
    paginator = Paginator(trabajadores, 10)
    try:
        trabajadores_page = paginator.page(page)
    except PageNotAnInteger:
        trabajadores_page = paginator.page(1)
    except EmptyPage:
        trabajadores_page = paginator.page(paginator.num_pages)

    return render(
        request,
        'lista_trabajadores.html',
        {
            'trabajadores': trabajadores_page,
            'page_obj': trabajadores_page,
            'paginator': paginator,
            'query': query,
            'filtro_estado': filtro_estado,
            'estado_options': [
                ('TODOS', 'Todos'),
                ('OBLIGATORIO', 'Obligatorio'),
                ('COMPLETO', 'Completo'),
            ],
        },
    )


@login_required
@user_passes_test(es_gestion_humana)
def eliminar_trabajador(request, trabajador_id):
    """Eliminar un trabajador y registrar el motivo en auditoría."""
    trabajador = get_object_or_404(Trabajador, id=trabajador_id)
    if request.method == 'POST':
        form = EliminarTrabajadorForm(request.POST)
        if form.is_valid():
            motivo = form.cleaned_data['motivo'].strip()
            if not motivo:
                form.add_error('motivo', 'Debe indicar el motivo de la eliminación.')
            else:
                detalles = (
                    f"Trabajador eliminado: {trabajador.user.get_full_name()} ({trabajador.cedula}). "
                    f"Motivo: {motivo}"
                )
                Auditoria.objects.create(
                    usuario=request.user,
                    accion='ELIMINACIÓN',
                    tabla_afectada='Trabajador',
                    registro_id=trabajador.id,
                    detalles=detalles,
                )
                # Eliminar también el usuario asociado para no dejar huellas de acceso.
                trabajador.user.delete()
                messages.success(request, 'Trabajador eliminado correctamente y motivo registrado en auditoría.')
                return redirect('lista_trabajadores')
    else:
        form = EliminarTrabajadorForm()

    return render(
        request,
        'eliminar_trabajador.html',
        {
            'trabajador': trabajador,
            'form': form,
        },
    )


@login_required
@user_passes_test(es_gestion_humana)
def editar_trabajador(request, trabajador_id):
    """Permite a admin corregir datos del trabajador."""
    trabajador = get_object_or_404(Trabajador, id=trabajador_id)
    if request.method == 'POST':
        form = TrabajadorEditForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
            Auditoria.objects.create(
                usuario=request.user,
                accion='EDICIÓN',
                tabla_afectada='Trabajador',
                registro_id=trabajador.id,
                detalles=(
                    f"Datos actualizados para {trabajador.user.get_full_name()} (Cédula: {trabajador.cedula})."
                ),
            )
            if form.cleaned_data.get('password'):
                messages.success(request, 'Datos guardados. La contraseña del trabajador se ha cambiado correctamente.')
            else:
                messages.success(request, 'Datos del trabajador actualizados correctamente.')
            return redirect('lista_trabajadores')
    else:
        form = TrabajadorEditForm(instance=trabajador)

    return render(request, 'editar_trabajador.html', {'form': form, 'trabajador': trabajador})


@login_required
@user_passes_test(es_gestion_humana)
def restablecer_contrasena(request, trabajador_id):
    """Permite a admin reiniciar la contraseña de un trabajador."""
    trabajador = get_object_or_404(Trabajador, id=trabajador_id)
    if request.method == 'POST':
        trabajador.user.set_password(settings.DEFAULT_PASSWORD)
        trabajador.user.save()
        trabajador.password_reset_required = True
        trabajador.save()
        Auditoria.objects.create(
            usuario=request.user,
            accion='RESET_PASSWORD',
            tabla_afectada='User',
            registro_id=trabajador.user.id,
            detalles=(
                f"Contraseña restablecida para {trabajador.user.get_full_name()} (Cédula: {trabajador.cedula})."
            ),
        )
        messages.success(
            request,
            f"La contraseña de {trabajador.user.username} se ha restablecido a '{settings.DEFAULT_PASSWORD}'. El trabajador debe cambiarla en su primer acceso.",
        )
        return redirect('lista_trabajadores')

    return render(request, 'restablecer_contrasena.html', {'trabajador': trabajador})


@login_required
def cambiar_contrasena(request):
    """Permite al usuario cambiar su contraseña y desactiva la obligación inicial."""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            if hasattr(user, 'trabajador'):
                trabajador = user.trabajador
                trabajador.password_reset_required = False
                trabajador.save()
            Auditoria.objects.create(
                usuario=user,
                accion='CAMBIO_CONTRASENA',
                tabla_afectada='User',
                registro_id=user.id,
                detalles='El usuario actualizó su contraseña.',
            )
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'cambiar_contrasena.html', {'form': form})


@login_required
def configuracion(request):
    """Página de configuración con opciones generales y administrativas."""
    # Si el usuario no es administrador, redirigimos directamente a cambiar_contrasena
    if not request.user.is_staff:
        return redirect('cambiar_contrasena')
    return render(request, 'configuracion.html', {'es_admin': request.user.is_staff})


@login_required
@user_passes_test(lambda u: u.is_staff)
def administrar_privilegios(request):
    """Permite a los administradores asignar o revocar privilegios de administrador."""
    query = request.GET.get('q', '').strip()
    trabajadores = Trabajador.objects.select_related('user').all().order_by('user__last_name')

    if query:
        trabajadores = trabajadores.filter(
            Q(cedula__icontains=query)
            | Q(user__first_name__icontains=query)
            | Q(user__last_name__icontains=query)
            | Q(user__email__icontains=query)
            | Q(cargo__icontains=query)
            | Q(departamento__icontains=query)
        )

    # Paginación: 10 trabajadores por página
    page = request.GET.get('page', 1)
    paginator = Paginator(trabajadores, 10)
    try:
        trabajadores_page = paginator.page(page)
    except PageNotAnInteger:
        trabajadores_page = paginator.page(1)
    except EmptyPage:
        trabajadores_page = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        action = request.POST.get('action')
        if user_id and action in ['grant', 'revoke']:
            try:
                trabajador = Trabajador.objects.select_related('user').get(user_id=int(user_id))
                target_user = trabajador.user
            except (Trabajador.DoesNotExist, ValueError):
                trabajador = None
                target_user = None

            if target_user is None:
                messages.error(request, 'Usuario no encontrado.')
            elif target_user == request.user and action == 'revoke':
                messages.error(request, 'No puedes quitarte privilegios a ti mismo desde esta página.')
            else:
                if action == 'grant':
                    target_user.is_staff = True
                    detalle = (
                        f'Privilegios de administrador otorgados a {target_user.get_full_name()} '
                        f'(Cédula: {trabajador.cedula}).'
                    )
                    messages.success(request, f'Se otorgaron privilegios a {target_user.get_full_name()}.')
                else:
                    target_user.is_staff = False
                    detalle = (
                        f'Privilegios de administrador revocados a {target_user.get_full_name()} '
                        f'(Cédula: {trabajador.cedula}).'
                    )
                    messages.success(request, f'Se revocaron privilegios a {target_user.get_full_name()}.')
                target_user.save()
                Auditoria.objects.create(
                    usuario=request.user,
                    accion='PRIVILEGIOS' if action == 'grant' else 'REVOCAR_PRIVILEGIOS',
                    tabla_afectada='User',
                    registro_id=target_user.id,
                    detalles=detalle,
                )
        else:
            messages.error(request, 'Solicitud inválida para la gestión de privilegios.')
        return redirect('privilegios')

    return render(
        request,
        'privilegios.html',
        {
            'trabajadores': trabajadores_page,
            'page_obj': trabajadores_page,
            'paginator': paginator,
            'query': query,
        },
    )


@login_required
def solicitar_permiso(request):
    """Permite al trabajador enviar una nueva solicitud con adjunto opcional."""
    if es_gestion_humana(request.user):
        return redirect('dashboard')

    trabajador = get_object_or_404(Trabajador, user=request.user)
    if request.method == 'POST':
        form = SolicitudForm(request.POST, request.FILES)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.trabajador = trabajador
            solicitud.save()
            Auditoria.objects.create(
                usuario=request.user,
                accion='CREACIÓN',
                tabla_afectada='Solicitud',
                registro_id=solicitud.id,
                detalles=(
                    f"El trabajador solicitó un {solicitud.tipo} desde {solicitud.fecha_inicio} "
                    f"hasta {solicitud.fecha_fin}."
                ),
            )
            return redirect('dashboard')
    else:
        form = SolicitudForm()

    return render(request, 'solicitar_permiso.html', {'form': form})


@login_required
@user_passes_test(es_gestion_humana)
def evaluar_solicitud(request, solicitud_id, accion):
    """Vista para aprobar o rechazar una solicitud con comentario obligatorio."""
    solicitud = get_object_or_404(Solicitud, id=solicitud_id)
    if accion not in ['aprobar', 'rechazar']:
        return redirect('dashboard')

    if request.method == 'POST':
        form = EvaluacionSolicitudForm(request.POST)
        if form.is_valid():
            observaciones = form.cleaned_data['observaciones_admin']
            solicitud.estado = 'APROBADO' if accion == 'aprobar' else 'RECHAZADO'
            solicitud.revisado_por = request.user
            solicitud.observaciones_admin = observaciones
            solicitud.save()
            Auditoria.objects.create(
                usuario=request.user,
                accion=accion.upper(),
                tabla_afectada='Solicitud',
                registro_id=solicitud.id,
                detalles=f"Solicitud ID {solicitud.id} cambiada a estado {solicitud.estado}. Obs: {observaciones}",
            )
            return redirect('dashboard')
    else:
        form = EvaluacionSolicitudForm(initial={'observaciones_admin': solicitud.observaciones_admin})

    return render(
        request,
        'evaluar_solicitud.html',
        {
            'solicitud': solicitud,
            'accion': accion,
            'form': form,
        },
    )


@login_required
@user_passes_test(es_gestion_humana)
def reporte_auditoria(request):
    """Muestra los logs de auditoría al personal autorizado."""
    query = request.GET.get('q', '').strip()
    logs = Auditoria.objects.select_related('usuario').all()
    if query:
        q_filter = (
            Q(usuario__username__icontains=query)
            | Q(usuario__first_name__icontains=query)
            | Q(usuario__last_name__icontains=query)
            | Q(accion__icontains=query)
            | Q(tabla_afectada__icontains=query)
            | Q(detalles__icontains=query)
        )
        # If query is numeric, also filter by registro_id
        if query.isdigit():
            q_filter = q_filter | Q(registro_id=int(query))
        logs = logs.filter(q_filter)

    # Paginación: 10 logs por página
    page = request.GET.get('page', 1)
    paginator = Paginator(logs, 10)
    try:
        logs_page = paginator.page(page)
    except PageNotAnInteger:
        logs_page = paginator.page(1)
    except EmptyPage:
        logs_page = paginator.page(paginator.num_pages)

    return render(request, 'reporte_auditoria.html', {'logs': logs_page, 'page_obj': logs_page, 'paginator': paginator, 'query': query})


def add_excel_header_image(hoja, workbook):
    encabezado_path = get_encabezado_path()
    if encabezado_path:
        try:
            from openpyxl.drawing.image import Image as ExcelImage
            img = ExcelImage(encabezado_path)
            img.width = 520
            img.height = 120
            hoja.add_image(img, 'A1')
            hoja.row_dimensions[1].height = 90
        except Exception:
            pass


def add_pdf_header_image(documento, ancho, alto):
    encabezado_path = get_encabezado_path()
    if encabezado_path:
        try:
            image_width = 420
            image_height = 100
            x = (ancho - image_width) / 2
            y = alto - image_height - 20
            documento.drawImage(encabezado_path, x, y, width=image_width, height=image_height, preserveAspectRatio=True, mask='auto')
        except Exception:
            pass


@login_required
@user_passes_test(es_gestion_humana)
def exportar_auditoria_excel(request):
    """Exporta el reporte de auditoría a Excel."""
    logs = Auditoria.objects.all()
    workbook = Workbook()
    hoja = workbook.active
    hoja.title = 'Auditoría'
    add_excel_header_image(hoja, workbook)

    hoja.append([])

    hoja.append(['Fecha/Hora', 'Usuario', 'Acción', 'Tabla', 'Registro', 'Detalles'])
    for log in logs:
        hoja.append([
            log.fecha_hora.strftime('%Y-%m-%d %H:%M:%S'),
            str(log.usuario),
            log.accion,
            log.tabla_afectada,
            log.registro_id,
            log.detalles,
        ])

    salida = BytesIO()
    workbook.save(salida)
    salida.seek(0)

    response = HttpResponse(
        salida.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename=auditoria.xlsx'
    return response


@login_required
@user_passes_test(es_gestion_humana)
def exportar_auditoria_pdf(request):
    """Exporta el reporte de auditoría a PDF."""
    logs = Auditoria.objects.all()
    buffer = BytesIO()
    documento = canvas.Canvas(buffer, pagesize=letter)
    ancho, alto = letter
    add_pdf_header_image(documento, ancho, alto)
    y = alto - 140
    documento.setFont('Helvetica-Bold', 12)
    documento.drawString(30, y, 'Reporte de Auditoría')
    y -= 30
    documento.setFont('Helvetica', 9)

    for log in logs:
        texto = (
            f"{log.fecha_hora:%Y-%m-%d %H:%M:%S} | {log.usuario} | {log.accion} | "
            f"{log.tabla_afectada} | {log.registro_id}"
        )
        documento.drawString(30, y, texto[:120])
        y -= 12
        documento.drawString(30, y, f"Detalles: {log.detalles[:120]}")
        y -= 20
        if y < 80:
            documento.showPage()
            add_pdf_header_image(documento, ancho, alto)
            documento.setFont('Helvetica', 9)
            y = alto - 140

    documento.save()
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=auditoria.pdf'
    return response


@login_required
@user_passes_test(es_gestion_humana)
def exportar_trabajadores_excel(request):
    """Exporta la lista de trabajadores a Excel."""
    trabajadores = Trabajador.objects.select_related('user').order_by('user__last_name')
    workbook = Workbook()
    hoja = workbook.active
    hoja.title = 'Trabajadores'
    add_excel_header_image(hoja, workbook)

    hoja.append([])

    hoja.append(['Cédula', 'Nombre', 'Correo', 'Cargo', 'Ubicación Administrativa', 'Cambio clave'])
    for trabajador in trabajadores:
        hoja.append([
            trabajador.cedula,
            trabajador.user.get_full_name(),
            trabajador.user.email,
            trabajador.cargo,
            trabajador.departamento,
            'Obligatorio' if trabajador.password_reset_required else 'Completo',
        ])

    salida = BytesIO()
    workbook.save(salida)
    salida.seek(0)
    response = HttpResponse(
        salida.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename=trabajadores.xlsx'
    return response


@login_required
@user_passes_test(es_gestion_humana)
def exportar_trabajadores_pdf(request):
    """Exporta la lista de trabajadores a PDF."""
    trabajadores = Trabajador.objects.select_related('user').order_by('user__last_name')
    buffer = BytesIO()
    documento = canvas.Canvas(buffer, pagesize=letter)
    ancho, alto = letter
    add_pdf_header_image(documento, ancho, alto)
    y = alto - 140
    documento.setFont('Helvetica-Bold', 12)
    documento.drawString(30, y, 'Lista de Trabajadores')
    y -= 30
    documento.setFont('Helvetica', 9)

    for trabajador in trabajadores:
        documento.drawString(30, y, f"{trabajador.cedula} | {trabajador.user.get_full_name()} | {trabajador.user.email}")
        y -= 12
        documento.drawString(30, y, f"{trabajador.cargo} | {trabajador.departamento} | {'Obligatorio' if trabajador.password_reset_required else 'Completo'}")
        y -= 20
        if y < 80:
            documento.showPage()
            add_pdf_header_image(documento, ancho, alto)
            documento.setFont('Helvetica', 9)
            y = alto - 140

    documento.save()
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=trabajadores.pdf'
    return response


class LoginView(auth_views.LoginView):
    template_name = 'login.html'
    authentication_form = CedulaAuthenticationForm


def logout_view(request):
    """Cerrar sesión y redirigir al login con next=/"""
    logout(request)
    return redirect('/login/?next=/')
