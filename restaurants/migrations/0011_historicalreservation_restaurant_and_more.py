# Generated by Django 4.2.7 on 2023-11-27 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0010_historicaltable_historicalstaff_historicalreview_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalreservation',
            name='restaurant',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='restaurants.restaurant', verbose_name='Ресторан'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant', verbose_name='Ресторан'),
            preserve_default=False,
        ),
    ]
