FROM python:3.12-slim

WORKDIR /app
COPY . /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFERED 1

ENV SECRET_KEY = '+lk=o)+5)pjlu+07cf)tgvx1)aw^6ijt%zj2(%m#8o=_d=ksq9'

RUN  pip install --upgrade pip
RUN pip install -r requirements/prod.txt
CMD python manage.py migrate \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; \
                                  User = get_user_model(); \
                                  User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@mail.com', 'admin')"\
    && python manage.py runserver 0.0.0.0:8000