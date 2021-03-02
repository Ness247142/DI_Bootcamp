from django.shortcuts import render
from .models import *


def home(request):
    gifs = Gif.objects.all()
    context = {'gifs': gifs}
    return render(request, 'main.html', context)

def gif_presentation(request, gif_id):
    gif = Gif.objects.get(id=gif_id)
    context = {'gif_app': gif}
    return render(request, 'gif_presentation.html', context)

def category(request):
    category_gif = Categories.objects.all()
    context = {'category': category_gif}
    return render(request, 'category.html', context)
