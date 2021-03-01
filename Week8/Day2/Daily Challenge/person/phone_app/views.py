from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def phonenumber(request):
    return HttpResponse('<h1>PhoneNumber page<h1>')


def name(request):
    return HttpResponse('<h1>Name page<h1>')
