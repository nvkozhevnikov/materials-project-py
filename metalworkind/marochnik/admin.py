from django.contrib import admin
from .models import *

@admin.register(Microstructures)
class MicrostructuresAdmin(admin.ModelAdmin):
    list_display = ('photo_alt', 'material', 'is_published', 'updated_at')

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)} # Автозаполнение slug
    list_display = ('name', 'is_published', 'updated_at')
    exclude = ['quantity_materials']

@admin.register(SubCategories)
class SubCategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'is_published', 'updated_at')
    exclude = ['quantity_materials']

@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'is_published', 'updated_at')
    list_filter = ('is_published',)

