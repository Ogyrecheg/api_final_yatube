from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Кастомные разрешения для пользователей."""

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        """Проверка прав пользователя на объект."""
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
