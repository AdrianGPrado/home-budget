from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)

def index_rtl(request):
    context = {}
    return render(request, 'index-rtl.html', context)

def charts(request):
    context = {}
    return render(request, 'charts.html', context)

def tables(request):
    context = {}
    return render(request, 'tables.html', context)

def blank_page(request):
    context = {}
    return render(request, 'blank-page.html', context)

def forms(request):
    context = {}
    return render(request, 'forms.html', context)

def bootstrap_elements(request):
    context = {}
    return render(request, 'bootstrap-elements.html', context)

def bootstrap_grid(request):
    context = {}
    return render(request, 'bootstrap-grid.html', context)
