# Generated by Django 4.1.1 on 2022-10-23 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_alter_contactformmodel_rating1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmodel',
            name='email',
            field=models.CharField(max_length=30, null=True, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contactformmodel',
            name='message',
            field=models.CharField(max_length=200, null=True, unique=True, verbose_name='Mesaj'),
        ),
        migrations.AlterField(
            model_name='contactformmodel',
            name='username',
            field=models.CharField(max_length=50, null=True, unique=True, verbose_name='Ad Soyad'),
        ),
    ]
