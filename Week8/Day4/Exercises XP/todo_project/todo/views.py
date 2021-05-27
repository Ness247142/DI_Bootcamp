from django.shortcuts import render, redirect, HttpResponse
from . import forms
from .models import User, Category, Todo
from django.contrib import messages

# Create your views here.


def signup(request):
    context = {
        'type': 'Sign Up',
        'form': forms.Signin_form()
    }

    if request.method == 'GET':
        return render(request, 'signin.html', context)

    else:
        filled_form = forms.Signin_form(request.POST)
        if filled_form.is_valid():
            new_user = filled_form.save()
            return redirect('display_to_do_list', new_user.id)
        else:
            messages.add_message(request, messages.INFO,
                                 'That username is already taken')
            return render(request, 'signin.html', {'form': filled_form})


def login(request):
    context = {
        'type': 'Log In',
        'form': forms.Login_form()
    }

    if request.method == 'GET':
        return render(request, 'signin.html', context)

    else:
        filled_form = forms.Login_form(request.POST)
        if filled_form.is_valid():
            try:
                user = User.objects.get(
                    username=filled_form.cleaned_data['username'], password=filled_form.cleaned_data['password'])
                return redirect('display_to_do_list', user.id)
            except:
                messages.add_message(
                    request, messages.WARNING, 'Username or password is incorrect')
                return render(request, 'signin.html', {'form': filled_form})
        else:
            messages.add_message(request, messages.WARNING,
                                 'Please enter valid information')
            return render(request, 'signin.html', {'form': filled_form})


def createTodo(request, userid):
    context = {
        'todo_form': forms.Create_todo_form(),
        'category_form': forms.Category_form()
    }
    current_user = User.objects.get(id=userid)
    if request.method == 'GET':
        return render(request, 'create_todo.html', context)
    else:
        filled_form = forms.Create_todo_form(request.POST)
        chosen_category = forms.Category_form(request.POST)
        if filled_form.is_valid() and chosen_category.is_valid():
            todo = filled_form.save(commit=False)
            todo.user = current_user
            todo.save()
            print(chosen_category.cleaned_data)
            category_object = Category.objects.get(
                id=chosen_category.cleaned_data['category'])
            category_object.todo_list.add(todo)
            return redirect('display_to_do_list', userid)
        else:
            context['todo_form'] = filled_form
            return render(request, 'signin.html', context)


def display_todos(request, userid):
    current_user = User.objects.get(id=userid)
    context = {
        'todos': current_user.todo_set.all()
    }
    return render(request, 'display_todos.html', context)
