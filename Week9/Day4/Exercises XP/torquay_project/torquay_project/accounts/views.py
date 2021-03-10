from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


class SignUpView(CreateView):
    form_class = UserSignupForm
    template_name = "registration/signup.html"
    success_url = 'home'

    def form_valid(self, form):
        super().form_valid(form)

        user = authenticate(self.request, username=form.cleaned_data['username'],
                            password=form.cleaned_data['password1'])

        login(self.request, user)
        return redirect(reverse(self.get_success_url()))


def login(request):
    if request.method == "GET":
        return render(request, 'registration/login.html', {'myform': LoginForm()})

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            return redirect('login')


def logout(request):
    logout(request)
    return redirect('home')
