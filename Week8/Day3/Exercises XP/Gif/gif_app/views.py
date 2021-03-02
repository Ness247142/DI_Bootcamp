from django.shortcuts import render
from django.http import HttpResponse


def category(request):
    return render(request, 'home.html', {'gif_app': Gif.objects.get(id=id)})


def categories(request):
    return render(request, 'home.html', {'gif_app': Gif.objects.get(id=id)})


def gif(request):
    return render(request, 'home.html', {'gif_app': Gif.objects.get(id=id)})
