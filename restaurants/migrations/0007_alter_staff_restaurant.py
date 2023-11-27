# Generated by Django 4.2.2 on 2023-06-20 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_staff_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant', verbose_name='Ресторан'),
        ),
    ]