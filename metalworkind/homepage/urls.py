from django.urls import path
from .views import *
from django.views.generic.base import TemplateView

app_name = 'homepage'
urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('subscribe/', subscribe, name='subscribe'),
    path('search/', Search.as_view(), name='search'),
    path('about/<slug:slug_about>/', about, name='about'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'),),
    path('yandex_77f8b102f26b1e8e.html', TemplateView.as_view(template_name='yandex_webmaster_confirmation', content_type='text/html'),),
    # path('test/', test, name='test'),
]

handler404 = "homepage.views.page_not_found_404"