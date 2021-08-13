from rest_framework import permissions

from api_yamdb.settings import ROLES


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated and request.user.role==ROLES[2][0]))

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.role==ROLES[2][0]


class IsAdmin(permissions.BasePermission):
    '''Доступ только администратору'''
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role==ROLES[2][0]

