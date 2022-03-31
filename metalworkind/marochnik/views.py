from django.views.generic import ListView
from .models import *

class Index(ListView):
    model = Categories
    template_name = 'marochnik/index.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Categories.objects.all()

class SubCategoriesAll(ListView):
    model = Categories
    template_name = 'marochnik/subcategory-all.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Categories.objects.filter(slug=self.kwargs['slug_category'])[0]
        context['subcategories'] = SubCategories.objects.filter(category=context['category'])
        context['materials'] = Materials.objects.filter(subcategory__in=context['subcategories'])
        return context

class SubCategoriesOne(ListView):
    model = SubCategories
    template_name = 'marochnik/subcategory-one.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategory'] = SubCategories.objects.filter(slug=self.kwargs['slug_subcategory'])[0]
        context['materials'] = Materials.objects.select_related('subcategory').filter(subcategory=context['subcategory'])
        return context

class Material(ListView):
    model = Materials
    template_name = 'marochnik/material.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Materials.objects.filter(slug=self.kwargs['slug_material'])[0]





