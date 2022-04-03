from django.contrib import admin
from .models import *


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    # Автозаполнение slug
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('h1', 'is_published', 'updated_at')

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('tag_name',)}
    list_display = ('tag_name', 'is_published', 'updated_at')

@admin.register(Spravochnik)
class SpravochnikAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('h1',)}
    list_display = ('h1', 'is_published', 'updated_at')