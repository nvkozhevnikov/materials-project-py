from django.views.generic import ListView
from django.shortcuts import redirect
from .utils import *
from django.http import Http404

from marochnik.services.count_quantity_materials_service import *

def test(request):
    count_quantity_materils_category()
    count_quantity_materils_subcategory()
    return redirect('/')

class Index(DataMixin, ListView):
    model = Categories
    template_name = 'marochnik/index.html'
    context_object_name = 'items'

    def get_queryset(self):
        try:
            categories = Categories.objects.all()
        except:
            raise Http404()
        return categories

class SubCategoriesList(DataMixin, ListView):
    model = Categories
    template_name = 'marochnik/subcategory-list.html'
    context_object_name = 'category'

    def get_queryset(self):
        try:
            categories = Categories.objects.filter(slug=self.kwargs['slug_category'])[0]
        except:
            raise Http404()
        return categories

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategories'] = SubCategories.objects.filter(category=context['category']).select_related('category')
        context['subcategory_all'] = 'ok'
        return context

class SubCategoriesOne(DataMixin, ListView):
    model = SubCategories
    template_name = 'marochnik/subcategory-one.html'
    context_object_name = 'subcategory'

    def get_queryset(self):
        try:
            subcategories = SubCategories.objects.select_related('category').filter(slug=self.kwargs['slug_subcategory'])[0]
        except:
            raise Http404()
        return subcategories

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['materials'] = Materials.objects.filter(subcategory=context['subcategory']).select_related('subcategory')
        context['subcategory_one'] = 'ok'
        context['category'] = context['subcategory'].category
        return context

class Material(DataMixin, ListView):
    model = Materials
    template_name = 'marochnik/material.html'
    context_object_name = 'items'

    def get_queryset(self):
        try:
            materials = Materials.objects.select_related('subcategory').filter(slug=self.kwargs['slug_material'])[0]
        except:
            raise Http404()
        return materials

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['microstructures'] = Microstructures.objects.filter(material__id=context['items'].pk)
        context['material_show'] = 'ok'
        return context





