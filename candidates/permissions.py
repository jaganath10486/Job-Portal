from rest_framework import permissions

class ISOwner(permissions.BasePermission):
    message = "You Don't have access to other Applied Candidates"
    def has_object_permission(self, request, view, obj):
        return (request.user == obj.candidate)
    
class isSuperUser(permissions.BasePermission):
    message = "You are an Employee You don't have access to Candidate  "
    def has_permission(self, request, view):
        return ~request.user.is_superuser