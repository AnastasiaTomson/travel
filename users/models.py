from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class CustomUser(AbstractBaseUser):
    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

    name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Фамилия")
    fathername = models.CharField(max_length=255, blank=True, null=True, verbose_name="Отчество")
    email = models.EmailField(blank=True, null=True, verbose_name="Эл. почта")
    last_login = models.DateTimeField(auto_now=True, verbose_name='Последнее время входа')
    username = models.CharField(max_length=35, unique=True)

    USERNAME_FIELD = 'username'

    @property
    def fio(self):
        return f'{self.last_name} {self.name}' if self.last_name else self.name
