from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'homepage/index.html', {
        'h1': 'Metalworkind',
    })

def about(request, slug_about):
    return render(request, 'homepage/about.html', {
        'h1': 'Metalworkind',
    })