from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('nik_name', 'photo', 'date_birth')
    list_filter = ('nik_name', 'date_birth')
    search_fields = ('nik_name', 'date_birth')
