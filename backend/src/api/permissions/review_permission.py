from rest_framework import permissions


class ReviewPermission(permissions.BasePermission):
    """Permission class that applies Read-Only status to reviews for
    all users except staff and the reviewer.

    Staff members are only permitted to delete reviews, not edit them.

    Only authenticated users may create reviews, and only for
    themselves.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method in ('POST',):
            return bool(
                request.user and request.user.is_authenticated
                and (request.user.id == int(request.data.get('user'))
                     if request.data.get('user') else True)
            )

        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method in ('DELETE',):
            return bool(request.user and (
                    request.user == obj.user
                    or request.user.is_staff
            ))

        return bool(request.user and (
                request.user == obj.user or request.user.is_superuser
        ))
