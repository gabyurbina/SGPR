import os, re, textwrap, zipfile
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

root = os.getcwd()
md_files = []
for dirpath, dirnames, filenames in os.walk(root):
    if '.git' in dirpath or 'venv' in dirpath or '.venv' in dirpath:
        continue
    # skip docs/pdfs and .venv
    if os.path.abspath(dirpath).startswith(os.path.abspath(os.path.join(root,'docs','pdfs'))):
        continue
    for f in filenames:
        if f.lower().endswith('.md'):
            md_files.append(os.path.join(dirpath,f))

out_dir = os.path.join(root, 'docs', 'pdfs')
os.makedirs(out_dir, exist_ok=True)

created = []
for md in md_files:
    try:
        try:
            with open(md, 'r', encoding='utf-8') as fh:
                text = fh.read()
        except:
            with open(md, 'r', encoding='latin-1') as fh:
                text = fh.read()
        # simple markdown to plain text
        text = re.sub(r'```.*?```', '', text, flags=re.S)
        text = re.sub(r'^#{1,6}\s*', '', text, flags=re.M)
        text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
        text = re.sub(r'\[(.*?)\]\((.*?)\)', r'\1 (\2)', text)
        text = text.replace('**','').replace('__','').replace('*','').replace('_','')
        text = re.sub(r'^\s*[-*+]\s+', '- ', text, flags=re.M)
        text = re.sub(r'\n{3,}', '\n\n', text)

        rel = os.path.splitext(os.path.relpath(md, root))[0]
        safe_name = rel.replace(os.sep, '_').replace('/', '_').replace('\\', '_')
        filename = safe_name + '.pdf'
        outpath = os.path.join(out_dir, filename)
        c = canvas.Canvas(outpath, pagesize=letter)
        width, height = letter
        margin = 50
        y_top = height - margin
        lines = []
        for paragraph in text.split('\n'):
            if paragraph.strip() == '':
                lines.append('')
                continue
            wrapped = textwrap.wrap(paragraph, 100)
            if not wrapped:
                lines.append('')
            else:
                lines.extend(wrapped)
        textobject = c.beginText()
        textobject.setTextOrigin(margin, y_top)
        textobject.setFont('Courier', 9)
        for line in lines:
            if textobject.getY() < margin:
                c.drawText(textobject)
                c.showPage()
                textobject = c.beginText()
                textobject.setTextOrigin(margin, y_top)
                textobject.setFont('Courier', 9)
            textobject.textLine(line)
        c.drawText(textobject)
        c.save()
        print('PDF_CREATED:'+outpath)
        created.append(outpath)
    except Exception as e:
        print('PDF_ERROR:'+md+':'+str(e))

zip_path = os.path.join(root, 'docs', 'SGPR_docs_pdfs.zip')
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    for p in created:
        arcname = os.path.relpath(p, os.path.join(root,'docs'))
        zf.write(p, arcname)
print('ZIP_CREATED:'+zip_path)
