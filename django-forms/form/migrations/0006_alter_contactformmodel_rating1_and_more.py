# Generated by Django 4.1.1 on 2022-10-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_alter_contactformmodel_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmodel',
            name='rating1',
            field=models.IntegerField(default=0, verbose_name='rating1'),
        ),
        migrations.AlterField(
            model_name='contactformmodel',
            name='rating2',
            field=models.IntegerField(default=0, verbose_name='rating2'),
        ),
    ]
