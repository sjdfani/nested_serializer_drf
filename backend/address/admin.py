from atexit import register
from django.contrib import admin
from .models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'zip_code', 'created', 'updated', 'state')
    list_editable = ('state',)