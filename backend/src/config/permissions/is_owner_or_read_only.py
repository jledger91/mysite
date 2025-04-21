from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Permission class that grants access to object owners."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user == obj.user)
