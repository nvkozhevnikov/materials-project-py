from django.urls import path
from .views import *

app_name = 'homepage'
urlpatterns = [
    path('', index, name='homepage'),
    path('subscribe/', subscribe, name='subscribe'),
    path('search/', search, name='search'),
    path('about/<slug:slug_about>/', about, name='about'),
]