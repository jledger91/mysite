from rest_framework import permissions


class IsSelfOrReadOnly(permissions.BasePermission):
    """Permission class that grants access to a user's own User
    object.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user == obj)
