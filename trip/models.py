from django.db import models
from users.models import CustomUser
from place.models import Place


# Маршруты
class Trip(models.Model):
    title = models.CharField(max_length=255, verbose_name='Маршрут')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)


# Пользовательские маршруты
class UserTrip(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=255, verbose_name='Маршрут')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    place = models.ManyToManyField(Place, verbose_name='Места')


# Избранное
class Favourite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    trip = models.ManyToManyField(Trip, verbose_name='Маршруты')
    place = models.ManyToManyField(Place, verbose_name='Места')
