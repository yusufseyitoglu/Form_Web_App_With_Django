# Generated by Django 4.1.1 on 2022-10-23 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0009_alter_contactformmodel_rating1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmodel',
            name='message',
            field=models.CharField(max_length=200, null=True, unique=True, verbose_name='Mesaj'),
        ),
        migrations.AlterField(
            model_name='contactformmodel',
            name='rating2',
            field=models.IntegerField(default=0, verbose_name='rating2'),
        ),
    ]