from django.urls import path
from .views import *

app_name = 'homepage'
urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('subscribe/', subscribe, name='subscribe'),
    path('search/', Search.as_view(), name='search'),
    path('about/<slug:slug_about>/', about, name='about'),
    path('test/', test, name='test'),
]