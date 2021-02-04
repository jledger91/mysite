from rest_framework import permissions


class SuperuserAllStaffReadOnly(permissions.BasePermission):
    """Permission class that applies Read-Only status to staff users
    and full permissions to superusers.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return bool(request.user and request.user.is_staff)

        return bool(request.user and request.user.is_superuser)
