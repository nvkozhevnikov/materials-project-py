from django.shortcuts import render
from django.views.generic import ListView

from .models import *

class Index(ListView):
    model = GostSections
    context_object_name = 'items'
    template_name = 'gosts/index.html'

    def get_queryset(self):
        return GostSections.objects.all()

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['h1'] = 'Справочник'
    #     return context

class ShowGostSection(ListView):
    model = GostSections
    context_object_name = 'items'
    template_name = 'gosts/gost-section.html'

    def get_queryset(self):
        return GostSections.objects.filter(slug=self.kwargs['slug_gost_section'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gost_section'] = 'ok'
        return context

class ShowGostGroup(ListView):
    model = GostSubSections
    context_object_name = 'items'
    template_name = 'gosts/gost-group.html'

    def get_queryset(self):
        return GostSubSections.objects.filter(slug=self.kwargs['slug_gost_group']).select_related('section')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gost_subsection'] = 'ok'
        return context

class ShowGost(ListView):
    model = Gosts
    context_object_name = 'items'
    template_name = 'gosts/gost-article.html'

    def get_queryset(self):
        return Gosts.objects.filter(slug=self.kwargs['slug_gost']).select_related('subsection')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gost_article'] = 'ok'
        return context

