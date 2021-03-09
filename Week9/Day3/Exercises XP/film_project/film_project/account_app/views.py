from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from cprint import cprint
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
    if request.method == "GET":
        my_form = LoginForm()
        return render(request, 'login.html', {'my_form': my_form})

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')

        else:
            return redirect('login')


def logout(request):
    logout(request)
    return redirect('homepage')


def profile(request):
    my_profile = User.objects.get(id=pk)
    return render(request, 'profile.html', {'my_profile': my_profile})
