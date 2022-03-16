from django.urls import path
from .views import *

app_name = 'gosts'
urlpatterns = [
    # path('<slug:slug_category>/<slug:slug_article>/', show_article, name='spravochnik-article-show'),
    path('', Index.as_view(), name='gosts-index-show'),
    path('<slug:slug_gost_section>', ShowGostSection.as_view(), name='gosts-section-show'),
]