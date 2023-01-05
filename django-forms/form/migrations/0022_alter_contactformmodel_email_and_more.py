# Generated by Django 4.1.1 on 2022-10-24 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0021_alter_contactformmodel_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmodel',
            name='email',
            field=models.CharField(max_length=30, null=True, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contactformmodel',
            name='username',
            field=models.CharField(max_length=50, null=True, unique=True, verbose_name='Ad Soyad'),
        ),
    ]