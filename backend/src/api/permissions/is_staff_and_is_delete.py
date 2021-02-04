from rest_framework import permissions


class IsStaffAndIsDelete(permissions.BasePermission):
    """Permission class that grants delete permission to staff."""

    def has_object_permission(self, request, view, obj):
        return request.method in ('DELETE',) and request.user.is_staff
