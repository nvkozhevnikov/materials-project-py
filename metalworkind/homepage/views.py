from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.db.models import Q
from .models import *
from marochnik.models import Materials
from spravochnik.models import Spravochnik
from gosts.models import Gosts
from .forms import *
from .sendinblue_services import subscribe_doi, send_transactional_email
from itertools import chain


def index(request):
    return render(request, 'homepage/index.html', {
        'h1': 'Metalworkind',
    })

def about(request, slug_about):
    page_data = get_object_or_404(About, slug=slug_about)
    if request.method == 'POST':
        form = AboutForm(request.POST)
        if form.is_valid():
            send_transactional_email(form.cleaned_data)
            return HttpResponseRedirect(request.path)
    else:
        form = AboutForm()

    return render(request, 'homepage/about.html', {
        'item': page_data,
        'form': form,
    })

def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subscribe_doi(form.cleaned_data['email'])

    return render(request, 'homepage/index.html', {
        'h1': 'Metalworkind',
    })

class Search(ListView):
    """ Поиск материалов """

    paginate_by = 10
    template_name = 'homepage/search-results.html'
    context_object_name = 'items'

    def get_queryset(self):
        materials = Materials.objects.prefetch_related('subcategory').filter(Q(name__icontains=self.request.GET.get('s')) |
                                                                             Q(name__icontains=self.request.GET.get('s'))
                                                                             )
        articles = Spravochnik.objects.select_related('category').filter(Q(post_introduction__icontains=self.request.GET.get('s')) |
                                                                         Q(post__icontains=self.request.GET.get('s'))
                                                                        )
        gosts = Gosts.objects.select_related('subsection').filter(Q(standard_number__icontains=self.request.GET.get('s')) |
                                                                  Q(title__icontains=self.request.GET.get('s'))
                                                                 )
        result = list(chain(materials, articles, gosts))
        return result

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s')
        return context
