from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    gifs = Gif.objects.all()
    context = {'gifs': gifs}
    return render(request, 'home.html', context)

def gif_presentation(request, gif_id):
    gifs = Gif.objects.get(id=gif_id)
    context = {'gifs': gifs}
    return render(request, 'gif_presentation.html', context)

def categories(request):
    pass
