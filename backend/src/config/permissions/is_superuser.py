from rest_framework import permissions


class IsSuperuser(permissions.BasePermission):
    """Permission class that applies full permissions to superusers."""

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser
