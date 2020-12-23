from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_id == request.user

class IsAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS and request.method == 'GET':
            return True
        return obj.user_id == request.user