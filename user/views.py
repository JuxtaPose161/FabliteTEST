from django.http import Http404
from django.contrib.auth import get_user_model
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from . import serializers, permissions

# Получаем модель пользователя
User = get_user_model()
class UserViewSet(ModelViewSet):
    """
    Класс представления, обеспечивает права на создание, получение, изменение и удаление данных:
    - не авторизованные: никакие данные
    - авторизованные: получение, изменение или удаление только своих данных
    - администраторы(superuser): создание, получение, изменение и удаление любых данных
    """
    queryset = User.objects.all()
    permission_classes = (permissions.IsAdminOrSelf, IsAuthenticated)
    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return serializers.UsersForAdminSerializer
        else:
            return serializers.UsersForUserSerializer
    def get_permissions(self):
        if self.action == 'list':
            return [IsAdminUser()]
        return super().get_permissions()
    def get_object(self):
        try:
            obj = super().get_object()
        except Http404:
            raise PermissionDenied()
        self.check_object_permissions(self.request, obj)
        return obj