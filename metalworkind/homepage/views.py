from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import *
from .forms import AboutForm

def index(request):
    return render(request, 'homepage/index.html', {
        'h1': 'Metalworkind',
    })

def about(request, slug_about):
    page_data = get_object_or_404(About, slug=slug_about)
    if request.method == 'POST':
        form = AboutForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(request.path)
    else:
        form = AboutForm()

    return render(request, 'homepage/about.html', {
        'h1': 'Metalworkind',
        'item': page_data,
        'form': form,
    })

def subscribe(request):
    return render(request, 'homepage/index.html', {
        'h1': 'Metalworkind',
    })

def search(request):
    return render(request, 'homepage/index.html', {
        'h1': 'Metalworkind',
    })