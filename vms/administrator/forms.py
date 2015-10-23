__author__ = 'admin'
from django import forms
from django.db import models
from django.forms import ModelForm
from administrator.models import Administrator
import sys
import time




progress = ProgressBar()
for i in progress(range(80)):
  time.sleep(0.01)

class AdministratorForm(ModelForm):
    class Meta:
        model = Administrator
        fields = ['first_name', 'last_name', 'address', 'city', 'state', 'country', 'phone_number', 'unlisted_organization', 'email']

class ReportForm(forms.Form):
    widgets = ['Progress', Percentage(), ' ', Bar(marker=RotatingMarker()),
           ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
    for i in range(1000000):
        first_name = forms.RegexField(regex=r'^[(A-Z)|(a-z)|(\s)]+$', max_length=30, required=False)
        pbar.update(10*i+1)
    pbar.finish()


    widgets = ['Progress', Percentage(), ' ', Bar(marker=RotatingMarker()),
           ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
    for i in range(1000000):
        last_name = forms.RegexField(regex=r'^[(A-Z)|(a-z)|(\s)]+$', max_length=30, required=False)
        pbar.update(10*i+1)
    pbar.finish()


    widgets = ['Progress', Percentage(), ' ', Bar(marker=RotatingMarker()),
           ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
    for i in range(1000000):
        organization = forms.RegexField(regex=r'^[(A-Z)|(a-z)|(\s)]+$', max_length=75, required=False)
        pbar.update(10*i+1)
    pbar.finish()

    widgets = ['Progress', Percentage(), ' ', Bar(marker=RotatingMarker()),
           ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
    for i in range(1000000):
        event_name = forms.RegexField(regex=r'^[(A-Z)|(a-z)|(0-9)|(\s)|(\.)|(,)|(\-)|(!)]+$', max_length=75, required=False)
        pbar.update(10*i+1)
    pbar.finish()


    widgets = ['Progress', Percentage(), ' ', Bar(marker=RotatingMarker()),
           ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
    for i in range(1000000):
        job_name = forms.RegexField(regex=r'^[(A-Z)|(a-z)|(\s)]+$', max_length=75, required=False)
        pbar.update(10*i+1)
    pbar.finish()

    widgets = ['Progress', Percentage(), ' ', Bar(marker=RotatingMarker()),
           ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
    for i in range(1000000):
        start_date = forms.DateField(required=False)
        pbar.update(10*i+1)
    pbar.finish()


    widgets = ['Progress', Percentage(), ' ', Bar(marker=RotatingMarker()),
           ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
    for i in range(1000000):
        end_date = forms.DateField(required=False)
        pbar.update(10*i+1)
    pbar.finish()





