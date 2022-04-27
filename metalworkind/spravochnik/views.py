from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .utils import *


class Index(DataMixin, ListView):
    template_name = 'spravochnik/index.html'

    def get_queryset(self):
        return Spravochnik.objects.all().order_by('-id').select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            context['page_number'] = int(self.request.GET['page'])
        context['title'] = 'Справочник'
        context['description'] = 'Справочник - статьи по металлам, металлообработке, справочные данные в машиностроении и смежных областях'

        return context


class ShowTag(DataMixin, ListView):
    template_name = 'spravochnik/tag.html'

    def get_queryset(self):
        return Spravochnik.objects.filter(tags__slug=self.kwargs['slug_tag']).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = context['items'][0].tags.all()[0]
        context['breadcrumb'] = {'name': tag.tag_name}
        context['tag'] = tag
        if self.request.GET:
            context['page_number'] = int(self.request.GET['page'])
        return context

class ShowCategory(DataMixin, ListView):
    template_name = 'spravochnik/category.html'

    def get_queryset(self):
        return Spravochnik.objects.filter(category__slug=self.kwargs['slug_category']).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context['items'][0].category
        context['breadcrumb'] = {'name': category.category_name}
        context['category'] = category
        if self.request.GET:
            context['page_number'] = int(self.request.GET['page'])
        return context


def show_article(request, slug_category, slug_article):
    article = get_object_or_404(Spravochnik, slug=slug_article)
    category = article.category
    breadcrumb = (
        {'url': category.get_absolute_url, 'name': category.category_name},
        {'url': None, 'name': article.h1},
    )

    return render(request, 'spravochnik/article.html', {
        'article': article,
        'breadcrumb': breadcrumb,
    })


