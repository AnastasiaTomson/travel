# Generated by Django 4.0.2 on 2022-04-26 06:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trip', '0003_remove_usertrip_place_userplace'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip', models.ManyToManyField(to='trip.Trip', verbose_name='Маршруты')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.DeleteModel(
            name='Favourite',
        ),
    ]
