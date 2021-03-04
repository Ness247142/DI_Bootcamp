from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo, Category
from django.http import Http404
from cprint import cprint
from .forms import TodoForm


def home(request):

    todo = Todo.objects.all()

    context = {
        'all_todos': todo,
    }

    html_page = render(request, 'home.html', context)

    return html_page


def todo(request):
    if request.method == "GET":
        myform = TodoForm()
        return render(request, 'add_todo.html', {'myform': myform})

    if request.method == "POST":

        myform = TodoForm(request.POST)

        if myform.is_valid():
            title = myform.cleaned_data['title']
            details = myform.cleaned_data['details']
            has_been_done = myform.cleaned_data['has_been_done']
            date_creation = myform.cleaned_data['date_creation']
            date_completion = myform.cleaned_data['date_completion']
            deadline_date = myform.cleaned_data['deadline_date']

            a1 = Todo(title=title,
                      details=details,
                      has_been_done=has_been_done,
                      date_creation=date_creation,
                      date_completion=date_completion,
                      deadline_date=deadline_date)
            a1.save()

            return redirect('todo')

        else:
            return render(request, 'add_todo.html', {'myform': myform})


def display_todos(request):
    return render(request, 'home.html')
