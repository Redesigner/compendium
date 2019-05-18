from django.shortcuts import render
from blog import nav
from . import email

def index(request):
    if request.POST:
        email.write_mail(request)

    return render(request, 'contact.html',  {'navitems' : nav.navitems})