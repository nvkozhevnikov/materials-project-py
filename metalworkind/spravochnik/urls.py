from django.urls import path
from .views import *

app_name = 'spravochnik'
urlpatterns = [
    path('', Index.as_view(), name='spravochnik-index-show'),
    path('tag/<slug:slug_tag>/', ShowTag.as_view(), name='spravochnik-tag-show'),
    path('<slug:slug_category>/', ShowCategory.as_view(), name='spravochnik-category-show'),
    path('<slug:slug_category>/<slug:slug_article>/', show_article, name='spravochnik-article-show'),
]