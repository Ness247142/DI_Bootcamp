from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from cprint import cprint
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages


def homepage(request):
    films = Film.objects.all()
    context = {
        'films': films,
    }
    return render(request, 'homepage.html', context)


def add_film(request):
    if request.method == "GET":
        myform = AddFilmForm()
        return render(request, 'add_film.html', {'myform': AddFilmForm()})

    if request.method == "POST":

        myform = AddFilmForm(request.POST)

        if myform.is_valid():
            myform.save()
            messages.success(request, 'Succesfully added!')
            return redirect('add_film')

        else:
            messages.error(request, 'An error occured. Please try again')
            return render(request, 'add_film.html', {'myform': myform})


def add_director(request):
    if request.method == "GET":
        return render(request, 'add_director.html', {'director': AddDirectorForm()})

    if request.method == 'POST':

        director = AddDirectorForm(request.POST)

        if director.is_valid():
            director.save()
            messages.success(request, 'Succesfully added!')
            return redirect('add_director')

        else:
            messages.error(request, 'An error occured. Please try again')
            return render(request, 'add_director.html', {'myform': myform})
