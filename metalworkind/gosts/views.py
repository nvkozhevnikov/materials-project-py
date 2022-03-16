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

