from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User


def home(request):
    return render(request, 'index.html')


@unauthorized
def registration(request):
    form = UserRegistration()
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.info(
                request, username + 'Your account was succesfully created. Login to continue')
            return redirect('registration/login.html')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


@unauthorized
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Your username or password is correct')

    return render(request, 'registration/login.html')


def logout(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    return render(request, 'registration/profile.html')
