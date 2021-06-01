from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, DetailView, CreateView, UpdateView

from film_app.forms import AddFilmForm, AddDirectorForm
from film_app.models import Director, Film

import requests

# Part I


def home(request):
    films = Film.objects.all()
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    chuck = response.json()
    return render(request, "homepage.html", {"films": films, "chuck": chuck["value"]})


# Part III-A
class Profile(DetailView):
    model = User
    template_name = "profile.html"


# Part II
class FilmUpdate(UpdateView):
    model = Film
    form_class = AddFilmForm
    template_name = "film/update_film.html"
    success_url = reverse_lazy("home")


# Part II
class DirectorUpdate(UpdateView):
    model = Director
    form_class = AddDirectorForm
    template_name = "director/update_director.html"
    success_url = reverse_lazy("home")


# Part I
def add_film(request):
    if request.method == "GET":
        form = AddFilmForm()
        return render(request, "film/add_film.html", {"form": form})

    if request.method == "POST":
        form = AddFilmForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = AddFilmForm()
    return render(request, "film/add_film.html", {"form": form})


# Part I
class AddDirector(CreateView):
    model = Director
    form_class = AddDirectorForm
    template_name = "director/add_director.html"
    success_url = reverse_lazy("home")
