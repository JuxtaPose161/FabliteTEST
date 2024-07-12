FROM python:3.12-slim

WORKDIR /app
COPY . /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFERED 1

ENV SECRET_KEY = '+lk=o)+5)pjlu+07cf)tgvx1)aw^6ijt%zj2(%m#8o=_d=ksq9'\
    DB_NAME = local_db\
    DB_USER = postgres\
    DB_USER_PASSWORD = root\
    DB_HOST = localhost\
    DB_PORT = 5432\
    ALLOWED_HOSTS = 'localhost, 0.0.0.0'

RUN pip install -r requirements/dev.txt
CMD python manage.py migrate \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; \
                                  User = get_user_model(); \
                                  User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@mail.com', 'admin')"\
    && python manage.py runserver 0.0.0.0:8000