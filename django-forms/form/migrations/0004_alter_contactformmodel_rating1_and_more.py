# Generated by Django 4.1.1 on 2022-10-18 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_contactformmodel_rating1_contactformmodel_rating2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmodel',
            name='rating1',
            field=models.IntegerField(null=True, unique=True, verbose_name='rating1'),
        ),
        migrations.AlterField(
            model_name='contactformmodel',
            name='rating2',
            field=models.IntegerField(null=True, unique=True, verbose_name='rating2'),
        ),
    ]
