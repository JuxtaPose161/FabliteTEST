from rest_framework import routers
from django.urls import path, include
from . import views

app_name = 'api'

router = routers.SimpleRouter()
router.register('user', views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls), name='user'),
    path('auth/', include('djoser.urls.authtoken')),
]
