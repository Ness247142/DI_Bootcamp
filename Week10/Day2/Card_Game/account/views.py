from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


def sign_up_view(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        profile_form = ProfileUpdateForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            form.save()
            # Stay logged in after signing up
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('profile')

    else:
        form = RegistrationForm()
        profile_form = ProfileUpdateForm()
        context = {
            'form': form,
            'profile_form': profile_form
        }
        return render(request, 'signup.html', context)


def login_view(request):

    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')

        else:
            messages.error(request, 'Username and/or password incorrect. Please try again')
            return redirect('login')

@login_required
def logout_view(request):

    logout(request)
    return redirect ('login')

@login_required
def profile_view(request):

    return render(request, 'profile.html')
    
@login_required
def profile_edit(request):

    if request.method == "GET":
        form1 = UserUpdateForm(instance=request.user)
        form2 = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'form1': form1,
            'form2': form2,
        }

        return render(request, 'profile_edit.html', context)

    if request.method == "POST":
        form1 = UserUpdateForm(request.POST, instance=request.user)
        form2 = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('profile')
    
    else:
        form1 = UserUpdateForm()
        form2 = ProfileUpdateForm()
        context = {
            'form1': form1,
            'form2': form2,
        }
        return render(request, 'profile_edit.html', context)