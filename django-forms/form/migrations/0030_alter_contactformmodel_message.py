# Generated by Django 4.1.1 on 2022-11-01 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0029_alter_contactformmodel_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmodel',
            name='message',
            field=models.CharField(blank=True, default='mesaj yok', max_length=200, verbose_name='Mesaj'),
        ),
    ]
