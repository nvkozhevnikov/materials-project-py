from django.urls import path
from .views import *

app_name = 'homepage'
urlpatterns = [
    path('', index, name='homepage'),
    path('about/<slug:slug_about>/', about, name='about'),
]