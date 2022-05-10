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
        i = random.randint(0, self.place.filter(image__isnull=False).distinct().count() - 1)
        return self.place.filter(image__isnull=False).distinct()[i].image.all()[0]

    def price(self):
        all_price = 0
        for place in self.place.all():
            all_price += place.price if place.price else 0
        return all_price


# Пользовательские маршруты
class UserTrip(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.title

    def place_in_trip(self):
        return [i.place.id for i in self.userplace_set.all()]

    def image(self):
        if self.userplace_set.exists():
            i = random.randint(0, self.userplace_set.filter(place__image__isnull=False).distinct().count() - 1)
            return self.userplace_set.filter(place__image__isnull=False).distinct()[i].place.image.all()[0]
        else:
            return None


# Пользовательские маршруты
class UserPlace(models.Model):
    trip = models.ForeignKey(UserTrip, on_delete=models.CASCADE, verbose_name='Тур')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Место')
    visit_date = models.DateField(blank=True, null=True, verbose_name='Дата')
    visit_time = models.TimeField(blank=True, null=True, verbose_name='Время')

    def __str__(self):
        return self.place.title


# Избранное
class FavouriteTrip(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, verbose_name='Маршруты')
