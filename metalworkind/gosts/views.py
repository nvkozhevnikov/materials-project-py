from django.views.generic import ListView
from .utils import *

from .models import *

class Index(DataMixin, ListView):
    model = GostSections
    context_object_name = 'items'
    template_name = 'gosts/index.html'
    allow_empty = False

    def get_queryset(self):
        return GostSections.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub_sections'] = GostSubSections.objects.filter(is_published=True)
        return context

class ShowGostSection(DataMixin, ListView):
    model = GostSections
    context_object_name = 'items'
    template_name = 'gosts/gost-section.html'
    allow_empty = False

    def get_queryset(self):
        return GostSections.objects.filter(slug=self.kwargs['slug_gost_section'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gost_section'] = 'ok'
        return context

class ShowGostGroup(DataMixin, ListView):
    model = GostSubSections
    context_object_name = 'items'
    template_name = 'gosts/gost-group.html'
    allow_empty = False

    def get_queryset(self):
        return GostSubSections.objects.filter(slug=self.kwargs['slug_gost_group']).select_related('section')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gost_subsection'] = 'ok'
        return context

class ShowGost(DataMixin, ListView):
    model = Gosts
    context_object_name = 'items'
    template_name = 'gosts/gost-article.html'
    allow_empty = False

    def get_queryset(self):
        return Gosts.objects.filter(slug=self.kwargs['slug_gost']).select_related('subsection')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gost_article'] = 'ok'
        return context

