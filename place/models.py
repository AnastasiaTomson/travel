from django.db import models


# Картинки
class Image(models.Model):
    img = models.ImageField(upload_to="place_image/", verbose_name="Изображение")
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)


# Теги
class Tag(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')


# Города
class City(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)


# Области
class District(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)


# Сезоны
class Season(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')


# Тип места
class TypePlace(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
