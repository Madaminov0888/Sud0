from django.contrib import admin
from .models import Working_Sites


@admin.register(Working_Sites)
class Working_Sites_Admin(admin.ModelAdmin):
    list_display = ['title', 'url', 'contact']
