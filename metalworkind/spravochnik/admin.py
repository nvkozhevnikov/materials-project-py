from django.contrib import admin
from .models import *


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    # Автозаполнение slug
    prepopulated_fields = {'slug': ('category_name',)}

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('tag_name',)}

@admin.register(Spravochnik)
class SpravochnikAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('h1',)}