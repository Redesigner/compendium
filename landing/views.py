from django.shortcuts import render

from . import nav

def index(request):
    return render(request, 'index.html',  {'navitems' : nav.navitems})