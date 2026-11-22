# Flormia Gift — catálogo floral (Django)

## Local (SQLite)
    python -m venv venv && venv\Scripts\activate   # Linux/Mac: source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate && python manage.py cargar_datos
    python manage.py createsuperuser
    python manage.py runserver

## Verificaciones
    python manage.py verificar_plantillas   # includes, extends y static
    python manage.py test

## Render
Build Command:
    pip install -r requirements.txt && python manage.py verificar_plantillas && python manage.py collectstatic --no-input && python manage.py migrate && python manage.py cargar_datos && (python manage.py createsuperuser --noinput || true)
Start Command:
    gunicorn config.wsgi:application
Variables: PYTHON_VERSION, SECRET_KEY, DATABASE_URL, DJANGO_SUPERUSER_USERNAME/EMAIL/PASSWORD.
Imágenes: guárdalas en static/img/<carpeta>/ y escribe la ruta (ej. img/ramos/pureza.jpg) en el admin.
