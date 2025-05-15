from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom Permission to only allow Owner to update"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
