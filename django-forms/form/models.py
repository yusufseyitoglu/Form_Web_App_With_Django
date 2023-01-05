from email.policy import default
from enum import auto, unique
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from xml.dom import ValidationErr
from django.db import models
from django.db import connections
from django import forms
# Create your models here.

class contactFormModel(models.Model):
    username = models.CharField(max_length=50, verbose_name='Ad Soyad',unique=False, null=True)
    email = models.CharField(max_length=30, verbose_name='Email',unique=True, null=True)
    message = models.CharField(max_length=200, verbose_name='Mesaj', unique=False, null=False, default="Mesaj Yok", blank=True)
    rating1 = models.IntegerField(verbose_name = 'rating1', unique=False, null=False, default=0, blank=True)
    rating2 = models.IntegerField(verbose_name = 'rating2', unique=False, null=False, default=0, blank=True)
    created_at = models.DateTimeField(verbose_name = 'Gönderilme Tarihi', auto_now = True)
    def clean(self):
        if not (self.message or self.rating1 and self.rating2):
            raise ValidationErr("Mesaj veya Puanlama girmek zorundasınız!")
    def __str__(self):
        return self.username
        