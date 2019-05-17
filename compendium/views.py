from django.shortcuts import render
from blog import nav

def index(request):
    return render(request, 'compendium.html', {'navitems' : nav.navitems})

def projects(request):
    return render(request, 'compendium.html')