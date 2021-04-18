from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import RedirectView

def index(request):
    return HttpResponse("<h1>Hello Srinivas</h1>You are getting better")

def data_flair(request):
    return redirect('/dataflair')


class tutorial(RedirectView): url = 'https://google.com'