from rest_framework.permissions import BasePermission
class IsAdminOrSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and (request.user.is_superuser or obj == request.user))