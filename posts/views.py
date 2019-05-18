from django.shortcuts import render
from blog import nav

def index(request):
    return render(request, 'posts.html',  {'navitems' : nav.navitems})