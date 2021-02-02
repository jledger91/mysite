from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    """Permission class that applies Read-Only status to
    all users except admins.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)
