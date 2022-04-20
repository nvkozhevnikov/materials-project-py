from django.urls import path
from .views import *

app_name = 'marochnik'
urlpatterns = [
    path('test/', test, name='test'),
    path('', Index.as_view(), name='marochnik-index-show'),
    path('<slug:slug_category>/', SubCategoriesList.as_view(), name='marochnik-subcategory-show'),
    path('<slug:slug_category>/<slug:slug_subcategory>/', SubCategoriesOne.as_view(), name='marochnik-subcategory-one-show'),
    path('<slug:slug_category>/<slug:slug_subcategory>/<slug:slug_material>/', Material.as_view(), name='marochnik-material-show'),
]