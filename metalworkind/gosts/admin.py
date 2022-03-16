from django.contrib import admin
from .models import *

@admin.register(GostSections)
class GostSectionsAdmin(admin.ModelAdmin):
    # Автозаполнение slug
    prepopulated_fields = {'slug': ('section_name',)}

@admin.register(GostSubSections)
class GostSubSectionsAdmin(admin.ModelAdmin):
    # Автозаполнение slug
    prepopulated_fields = {'slug': ('subsection_name',)}

@admin.register(Gosts)
class GostsAdmin(admin.ModelAdmin):
    # Автозаполнение slug
    prepopulated_fields = {'slug': ('h1',)}
