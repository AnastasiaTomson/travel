from django.contrib.auth.backends import BaseBackend, ModelBackend

from users.models import CustomUser
from django.contrib.auth.hashers import check_password


class SettingsBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username and password:
            try:
                user = CustomUser.objects.get(username=username)
                if check_password(password, user.password):
                    return user
            except CustomUser.DoesNotExist:
                pass
        return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
