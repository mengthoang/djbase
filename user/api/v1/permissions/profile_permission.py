from rest_framework.permissions import BasePermission

class IsAdminUserOrProfileOwner(BasePermission):
    """
    Allows access only to admin users or profile owner.
    """
    
    def has_object_permission(self, request, _view, obj):
        return bool(request.user and request.user.is_staff) \
            or request.user == obj.user
