# Generated by Django 4.2.2 on 2023-06-20 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant', verbose_name='Ресторан'),
        ),
    ]
