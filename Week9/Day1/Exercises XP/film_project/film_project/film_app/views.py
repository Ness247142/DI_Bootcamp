from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views import generic
from django.urls import reverse_lazy


def homepage(request):
    films = Film.objects.all()
    context = {
        'films': films,
    }
    return render(request, 'homepage.html', context)


def add_film(request):
    if request.method == "GET":
        myform = AddFilmForm()
        return render(request, 'add_film.html', {'myform': myform})

    if request.method == "POST":

        myform = AddFilmForm(request.POST)

        if myform.is_valid():
            myform.save()
            return redirect('homepage')

        else:
            return render(request, 'add_film.html', {'myform': myform})


def AddDirector(CreateView):
    form_class = AddDirectorForm
    template_name = 'add_director.html'
    success_url = reverse_lazy('homepage.html')
