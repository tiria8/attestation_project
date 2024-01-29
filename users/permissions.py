from rest_framework.permissions import BasePermission


class IsActive(BasePermission):
    """ Класс для создания прав доступа к API только для активных пользователей"""

    def has_object_permission(self, request, view, obj):

        if request.user.is_active:
            return True

        return False
