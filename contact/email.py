from django import forms
from django.core.mail import send_mail

class MailForm(forms.Form):
    name = forms.CharField(label = 'name', max_length = 125)
    address = forms.CharField(label = 'address', max_length = 255)
    message = forms.CharField(label = 'message', max_length = 4095)

def write_mail(request):
    form = MailForm(request.POST)
    if form.is_valid():
        send_mail(
            'Contact from: ' + form.name,
            form.message + '/br via site',
            form.address,
            'stephenwmelnick@gmail.com',
            False
        )
    return