from django.shortcuts import render, get_object_or_404
from .models import *

def index(request):
    return render(request, 'homepage/index.html', {
        'h1': 'Metalworkind',
    })

def about(request, slug_about):
    page_data = get_object_or_404(About, slug=slug_about)

    return render(request, 'homepage/about.html', {
        'h1': 'Metalworkind',
        'item': page_data,
    })