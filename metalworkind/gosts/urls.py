from django.urls import path
from .views import *

app_name = 'gosts'
urlpatterns = [
    path('', Index.as_view(), name='gosts-index-show'),
    path('<slug:slug_gost_section>/', ShowGostSection.as_view(), name='gosts-section-show'),
    path('<slug:slug_gost_section>/<slug:slug_gost_group>/', ShowGostGroup.as_view(), name='gosts-group-show'),
    path('<slug:slug_gost_section>/<slug:slug_gost_group>/<slug:slug_gost>/', ShowGost.as_view(), name='gosts-article-show'),

]