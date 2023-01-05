from django.contrib import admin
from form.models import contactFormModel


class contactFormModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'message','rating1','rating2','created_at')

admin.site.register(contactFormModel,contactFormModelAdmin)