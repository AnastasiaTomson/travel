# Generated by Django 4.0.2 on 2022-05-10 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0008_alter_userplace_visit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userplace',
            name='visit_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Время'),
        ),
    ]
