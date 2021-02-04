from rest_framework import permissions


class IsUnauthenticatedAndIsCreate(permissions.BasePermission):
    """Permission class that allows creation only to unauthenticated
    users.
    """

    def has_permission(self, request, view):
        if request.method in ('POST',):
            return True

        return request.user and request.user.is_authenticated
