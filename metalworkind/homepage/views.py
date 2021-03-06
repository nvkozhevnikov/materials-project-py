from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.db.models import Q
from .models import *
from marochnik.models import Materials
from spravochnik.models import Spravochnik
from gosts.models import Gosts
from .forms import *
from itertools import chain
from datetime import datetime, timedelta

# from homepage.services.sendinblue_service import subscribe_doi, send_transactional_email
from .services.cbr_exchange_rate_service import get_usd_rate
from .services.get_metal_prices_service import get_metal_prices
from .services.news_parser_service import get_news
from .tasks import subscribe_doi_sendinblue, send_transaction_email_sendinblue

def download_data_everyday():
    get_news()
    get_metal_prices()
    get_usd_rate()
    return None

def page_not_found_404(request, exception):
    return render(request, 'homepage/404.html', status=404)


class Index(ListView):
    template_name = 'homepage/index.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Spravochnik.objects.select_related('category').all().order_by('-id')[:8]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['metal_prices'] = MetalPrices.objects.all()
        context['news'] = News.objects.filter(published_date__gt=datetime.now().date() - timedelta(days=30)).order_by('-id')[:10]
        context['usd_exchange_rate'] = ExchangeRates.objects.filter(currency__name='USD').order_by('-id')[:1][0]
        return context

def about(request, slug_about):
    page_data = get_object_or_404(About, slug=slug_about)
    if request.method == 'POST':
        form = AboutForm(request.POST)
        if form.is_valid():
            send_transaction_email_sendinblue.delay(form.cleaned_data)
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
            subscribe_doi_sendinblue.delay(form.cleaned_data['email'])

    return redirect('/')

class Search(ListView):
    """ ?????????? ???????????????????? """

    paginate_by = 10
    template_name = 'homepage/search-results.html'
    context_object_name = 'items'

    def get_queryset(self):
        materials = Materials.objects.select_related('subcategory').filter(Q(name__icontains=self.request.GET.get('s')) |
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



