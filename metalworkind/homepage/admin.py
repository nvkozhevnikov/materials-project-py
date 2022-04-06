from django.contrib import admin
from .models import *

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    # Автозаполнение slug
    prepopulated_fields = {'slug': ('h1',)}

@admin.register(MetalPrices)
class MetalPricesAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit', 'price', 'created_at')

@admin.register(Currencies)
class CurrenciesAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'updated_at')

@admin.register(ExchangeRates)
class ExchangeRatesAdmin(admin.ModelAdmin):
    list_display = ('currency', 'price', 'date')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('get_title_admin_panel', 'source', 'created_at')
