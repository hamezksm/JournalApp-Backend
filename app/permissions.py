from rest_framework import permissions

# Create your permissions here.

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permissions that only allow owners of an object to edit it
    """
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for  any request
        # so, we'll allow GET, HEAD and OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write Permissions are only allowed to the owner/user  of the object.
        return obj.user == request.user