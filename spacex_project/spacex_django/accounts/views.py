from django.shortcuts import render, redirect
from .forms import UserSignupForm
from django.views.generic import CreateView
from django.urls import reverse
from django.contrib.auth import authenticate, login


class SignUpView(CreateView):
    form_class = UserSignupForm
    template_name = 'registration/signup.html'
    success_url = 'home'

    def form_valid(self, form):
        # Populates the form with the POST data, validates it and saves the object (User) to the database
        super().form_valid(form)
        
        # get that user object out of the database
        user = authenticate(self.request, username=form.cleaned_data['username'], 
                                          password=form.cleaned_data['password1'])
        # create a session / cookie
        login(self.request, user)

        # take them to the success url
        return redirect(reverse(self.get_success_url()))
