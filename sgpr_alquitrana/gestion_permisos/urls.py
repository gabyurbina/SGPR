from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('registro/', views.registro_trabajador, name='registro_trabajador'),
    path('solicitar/', views.solicitar_permiso, name='solicitar_permiso'),
    path('cambiar-contrasena/', views.cambiar_contrasena, name='cambiar_contrasena'),
    path('configuracion/', views.configuracion, name='configuracion'),
    path('configuracion/privilegios/', views.administrar_privilegios, name='privilegios'),
    path('api/trabajadores/registro/', views.api_registro_trabajador, name='api_registro_trabajador'),
    path('trabajadores/', views.lista_trabajadores, name='lista_trabajadores'),
    path('trabajadores/<int:trabajador_id>/editar/', views.editar_trabajador, name='editar_trabajador'),
    path('trabajadores/<int:trabajador_id>/restablecer/', views.restablecer_contrasena, name='restablecer_contrasena'),
    path('trabajadores/<int:trabajador_id>/eliminar/', views.eliminar_trabajador, name='eliminar_trabajador'),
    path('evaluar/<int:solicitud_id>/<str:accion>/', views.evaluar_solicitud, name='evaluar_solicitud'),
    path('auditoria/', views.reporte_auditoria, name='reporte_auditoria'),
    path('auditoria/descargar/xlsx/', views.exportar_auditoria_excel, name='exportar_auditoria_excel'),
    path('auditoria/descargar/pdf/', views.exportar_auditoria_pdf, name='exportar_auditoria_pdf'),
    path('trabajadores/descargar/xlsx/', views.exportar_trabajadores_excel, name='exportar_trabajadores_excel'),
    path('trabajadores/descargar/pdf/', views.exportar_trabajadores_pdf, name='exportar_trabajadores_pdf'),
]
