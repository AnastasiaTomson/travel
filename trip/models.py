from django.db import models
from users.models import CustomUser

# Маршруты
class Trip(models.Model):
    title = models.CharField(max_length=255, verbose_name='Маршрут')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)


# Избранные маршруты
class FavouriteTrip(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, verbose_name='Маршрут')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')


# Пользовательские маршруты
class UserTrip(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=255, verbose_name='Маршрут')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
