from django.contrib import admin
from main.models import *


class RegisterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'stream', 'phone', 'date_joined')
    list_display_links = ('first_name', 'email', 'stream', 'phone')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'date_of_contact')
    list_display_links = ('full_name', 'email', 'phone', 'date_of_contact')


class Tap_modelAdmin(admin.ModelAdmin):
    list_display = ('job_title',)
    list_display_links = ('job_title',)


admin.site.register(Register, RegisterAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Tap_model, Tap_modelAdmin)
