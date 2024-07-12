from rest_framework import routers
from django.urls import path, include
from . import views

app_name = 'api'

router = routers.SimpleRouter()
router.register('user', views.UserViewSet, basename='users')

urlpatterns = [

    # Созданные нашим представлением маршруты /api/user/ и /api/user/<pk:int>
    path('', include(router.urls), name='user'),

    # Маршруты из Djoser для авторизации пользователя, подробнее по ссылке:
    # See https://djoser.readthedocs.io/en/latest/token_endpoints.html
    path('auth/', include('djoser.urls.authtoken')),
]
