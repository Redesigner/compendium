from django.shortcuts import render

from blog import nav

def index(request):
    return render(request, 'index.html',  {'navitems' : nav.navitems})