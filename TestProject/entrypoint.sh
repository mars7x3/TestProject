python manage.py collectstatic --noinput
daphne main.asgi:application -b 0.0.0.0 -p 8000
