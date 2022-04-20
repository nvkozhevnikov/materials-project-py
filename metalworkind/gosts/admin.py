from django.contrib import admin
from .models import *

@admin.register(GostSections)
class GostSectionsAdmin(admin.ModelAdmin):
    # Автозаполнение slug
    prepopulated_fields = {'slug': ('section_name',)}
    list_display = ('section_number', 'section_name', 'is_published', 'updated_at')

@admin.register(GostSubSections)
class GostSubSectionsAdmin(admin.ModelAdmin):
    # Автозаполнение slug
    prepopulated_fields = {'slug': ('subsection_name',)}
    list_display = ('subsection_group', 'subsection_name', 'is_published', 'updated_at')

@admin.register(Gosts)
class GostsAdmin(admin.ModelAdmin):
    # Автозаполнение slug
    prepopulated_fields = {'slug': ('standard', 'standard_number',)}
    list_display = ('standard', 'standard_number', 'is_published', 'updated_at')
