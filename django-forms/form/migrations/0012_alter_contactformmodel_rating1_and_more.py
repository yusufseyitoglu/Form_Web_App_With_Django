# Generated by Django 4.1.1 on 2022-10-23 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0011_alter_contactformmodel_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmodel',
            name='rating1',
            field=models.CharField(max_length=200, null=True, verbose_name='rating1'),
        ),
        migrations.AlterField(
            model_name='contactformmodel',
            name='rating2',
            field=models.CharField(max_length=200, null=True, verbose_name='rating2'),
        ),
    ]