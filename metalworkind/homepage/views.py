from django.shortcuts import render

def index(request):
    return render(request, 'spravochnik/index.html', {
        'h1': 'Metalworkind',
    })
