from django.db import models
from users.models import *


# Картинки
class Image(models.Model):
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображение'

    img = models.ImageField(upload_to="place_image/", verbose_name="Изображение")
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.title


# Теги
class Tag(models.Model):
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Тег'

    title = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.title


# Города
class City(models.Model):
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Город'

    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.title


# Области
class District(models.Model):
    class Meta:
        verbose_name = 'Области'
        verbose_name_plural = 'Области'

    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.title


# Сезоны
class Season(models.Model):
    class Meta:
        verbose_name = 'Сезоны'
        verbose_name_plural = 'Сезоны'

    title = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.title


# Тип места
class TypePlace(models.Model):
    class Meta:
        verbose_name = 'Тип места'
        verbose_name_plural = 'Тип места'

    title = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.title


# Контакты
class Contact(models.Model):
    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    fb = models.URLField(verbose_name='Фейсбук', blank=True, null=True)
    vk = models.URLField(verbose_name='ВКонтакте', blank=True, null=True)
    inst = models.URLField(verbose_name='Инстаграм', blank=True, null=True)
    site = models.URLField(verbose_name='Сайт', blank=True, null=True)
    phone = models.TextField(verbose_name='Телефон', blank=True, null=True)
    phone1 = models.TextField(verbose_name='Доп. телефон', blank=True, null=True)
    phone2 = models.TextField(verbose_name='Доп. телефон', blank=True, null=True)
    phone3 = models.TextField(verbose_name='Доп. телефон', blank=True, null=True)
    email = models.EmailField(verbose_name='Почта', blank=True, null=True)

    def __str__(self):
        return self.phone


# Время работы
class TimeOfWork(models.Model):
    class Meta:
        verbose_name = 'Время работы'
        verbose_name_plural = 'Время работы'

    weekday = models.CharField(max_length=50, choices=[('1', 'Понедельник'),
                                                       ('2', 'Вторник'),
                                                       ('3', 'Среда'),
                                                       ('4', 'Четверг'),
                                                       ('5', 'Пятница'),
                                                       ('6', 'Суббота'),
                                                       ('7', 'Воскресенье')],
                               verbose_name='День недели')

    start_time = models.TimeField(blank=True, null=True, verbose_name='Начало работы')
    end_time = models.TimeField(blank=True, null=True, verbose_name='Окончание работы')
    place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name='Место')

    def __str__(self):
        return f"{self.place} - {self.get_weekday_display()}"


# Место
class Place(models.Model):
    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Место'

    title = models.CharField(max_length=255, verbose_name='Место')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    address = models.TextField(verbose_name='Адрес', blank=True, null=True)
    coordinates = models.TextField(verbose_name='Координаты')
    price = models.FloatField(verbose_name='Цена', blank=True, null=True)
    city = models.ForeignKey(City, verbose_name='Город', on_delete=models.CASCADE, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name='Район')
    season = models.ForeignKey(Season, on_delete=models.CASCADE, verbose_name='Сезон')
    tag = models.ManyToManyField(Tag, verbose_name='Теги', blank=True)
    type = models.ForeignKey(TypePlace, verbose_name='Тип места', on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, verbose_name='Контакты', null=True, blank=True)
    image = models.ManyToManyField(Image, verbose_name='Изображения', blank=True)

    def __str__(self):
        return f'{self.title} ({self.city})'

    def one_image(self):
        return self.image.all()[0]


# Избранное
class FavouritePlace(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Места')
