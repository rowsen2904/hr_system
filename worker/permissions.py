from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsSuperUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user:
            if request.user.is_superuser:
                return True
            if request.user.is_staff:
                return bool(request.method in SAFE_METHODS)

        return False
