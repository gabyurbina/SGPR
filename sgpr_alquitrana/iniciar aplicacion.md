PowerShell

cd D:\Users\urbinag\SGPR\sgpr_alquitrana
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver