# Generated by Django 4.0.2 on 2022-04-26 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0004_favouritetrip_delete_favourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favouritetrip',
            name='trip',
        ),
        migrations.AddField(
            model_name='favouritetrip',
            name='trip',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='trip.trip', verbose_name='Маршруты'),
            preserve_default=False,
        ),
    ]
