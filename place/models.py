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


# Контакты
class Contact(models.Model):
    fb = models.URLField(verbose_name='Фейсбук', blank=True, null=True)
    vk = models.URLField(verbose_name='ВКонтакте', blank=True, null=True)
    inst = models.URLField(verbose_name='Инстаграм', blank=True, null=True)
    site = models.URLField(verbose_name='Сайт', blank=True, null=True)
    phone = models.TextField(verbose_name='Телефон', blank=True, null=True)
    phone1 = models.TextField(verbose_name='Доп. телефон', blank=True, null=True)
    phone2 = models.TextField(verbose_name='Доп. телефон', blank=True, null=True)
    phone3 = models.TextField(verbose_name='Доп. телефон', blank=True, null=True)
    email = models.EmailField(verbose_name='Почта', blank=True, null=True)


# Время работы
class TimeOfWork(models.Model):
    monday_start = models.TimeField(blank=True, null=True, verbose_name='Начало приема заказов в понедельник')
    monday_end = models.TimeField(blank=True, null=True, verbose_name='Окончание приема заказов в понедельник')
    monday_is_day_off = models.BooleanField(default=False, verbose_name='Понедельник выходной?')

    tuesday_start = models.TimeField(blank=True, null=True, verbose_name='Начало приема заказов во вторник')
    tuesday_end = models.TimeField(blank=True, null=True, verbose_name='Окончание приема заказов во вторник')
    tuesday_is_day_off = models.BooleanField(default=False, verbose_name='Вторник выходной?')

    wednesday_start = models.TimeField(blank=True, null=True, verbose_name='Начало приема заказов в среду')
    wednesday_end = models.TimeField(blank=True, null=True, verbose_name='Окончание приема заказов в среду')
    wednesday_is_day_off = models.BooleanField(default=False, verbose_name='Среда выходной?')

    thursday_start = models.TimeField(blank=True, null=True, verbose_name='Начало приема заказов в четверг')
    thursday_end = models.TimeField(blank=True, null=True, verbose_name='Окончание приема заказов в четверг')
    thursday_is_day_off = models.BooleanField(default=False, verbose_name='Четверг выходной?')

    friday_start = models.TimeField(blank=True, null=True, verbose_name='Начало приема заказов в пятницу')
    friday_end = models.TimeField(blank=True, null=True, verbose_name='Окончание приема заказов в пятницу')
    friday_is_day_off = models.BooleanField(default=False, verbose_name='Пятница выходной?')

    saturday_start = models.TimeField(blank=True, null=True, verbose_name='Начало приема заказов в субботу')
    saturday_end = models.TimeField(blank=True, null=True, verbose_name='Окончание приема заказов в субботу')
    saturday_is_day_off = models.BooleanField(default=False, verbose_name='Суббота выходной?')

    sunday_start = models.TimeField(blank=True, null=True, verbose_name='Начало приема заказов в воскресенье')
    sunday_end = models.TimeField(blank=True, null=True, verbose_name='Окончание приема заказов в воскресенье')
    sunday_is_day_off = models.BooleanField(default=False, verbose_name='Воскресенье выходной?')