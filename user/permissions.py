from rest_framework.permissions import BasePermission
class IsAdminOrSelf(BasePermission):
    """
    Кастомный permission для того, чтобы обычные пользователи не могли смотреть другие профили
    """
    def has_object_permission(self, request, view, obj):
        return bool(request.user and (request.user.is_superuser or obj == request.user))