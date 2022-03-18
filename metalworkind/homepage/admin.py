from django.contrib import admin
from .models import *

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    # Автозаполнение slug
    prepopulated_fields = {'slug': ('h1',)}
