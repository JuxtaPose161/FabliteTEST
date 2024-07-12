# Auth-приложение на Django
Тестовое серверное приложение для авторизации с помощью токенов через HTTP-запросы

## Запуск 
### Запуск через Docker
1. Клонируем репозиторий
2. Устанавливаем [Docker](https://docs.docker.com/engine/install/) и [Docker-compose](https://docs.docker.com/compose/install/)
3. С помощью командной строки заходим в директорию (папку) проекта
4. Выполняем команду:
#### 
    docker compose up --build
### Запуск через редактор кода
1. Заменяем в `settings.py` переменную `DATABASE` на
####
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        } 
    }
2. Создаём виртуальное окружение и активируем его
3. Устанавливаем библиотеки:
####
    pip install -r requirements\dev.txt
4. В командной строке последовательно выполняем:
####
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000

#### В обоих случаях будет открыт хост на порту `0.0.0.0:8000`, к которому можно обращаться с помощью HTTP-запросов. 
## Список базовых маршрутов
* Создание пользователя (после создание вернётся JSON с данными, **запомните оттуда свой ID**)
####
    POST /auth/users/ 

    `Body: {"username": "your_username", "password": "your_password"}`

* Получение токена авторизации (он придёт ответом на запрос)
####
    POST /api/auth/token/login/ 

    `Body: {"username": "your_username", "password": "your_password"}`
* Удаление токена авторизации
####
    POST /api/auth/token/logout/ 
* Получение, редактирование и удаление записи (получение можно без `Body`)
####
    GET PUT DELETE /api/user/<your_id>/

    `Header: {"Authorization": "Token <auth_token>"}'`
    `Body: {"username": "your_username", "password": "your_password", "other_fields": "values"}`
* Получение всех записей (только для администрации)
####
    GET /api/user/

    `Header: {"Authorization": "Token <auth_token>"}`