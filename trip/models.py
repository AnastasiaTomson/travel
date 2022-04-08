from django.db import models
from users.models import MyUser
from place.models import Place
import random


# Маршруты
class Trip(models.Model):
    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Тур'

    title = models.CharField(max_length=255, verbose_name='Маршрут')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    place = models.ManyToManyField(Place, verbose_name='Места')

    def __str__(self):
        return self.title

    def image(self):
        i = random.randint(0, self.place.count() - 1)
        return self.place.all()[i].image

    def price(self):
        all_price = 0
        for place in self.place.all():
            all_price += place.price if place.price else 0
        return all_price


# Пользовательские маршруты
class UserTrip(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=255, verbose_name='Маршрут')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    place = models.ManyToManyField(Place, verbose_name='Места')

    def __str__(self):
        return self.title


# Избранное
class Favourite(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    trip = models.ManyToManyField(Trip, verbose_name='Маршруты')
    place = models.ManyToManyField(Place, verbose_name='Места')
