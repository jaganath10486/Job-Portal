from rest_framework import permissions

class isSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request)
        return request.user.is_superuser
    
class IsOwner(permissions.BasePermission):
    message = "You Don't have access to access other Job Posts"
    def has_object_permission(self, request, view, obj):
        return request.user == obj.creator
