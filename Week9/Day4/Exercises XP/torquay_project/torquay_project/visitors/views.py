from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.http import Http404
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def info(request):
    pass


class BookingView(ListView):
    pass
