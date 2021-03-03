from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Mission, Astro
from django.http import Http404
from cprint import cprint
from .forms import AddAstroForm

def home(request):

    missions = Mission.objects.all()

    context = {
        'all_missions': missions,
        'director': 'Paul Tomkins'
    }

    html_page = render(request, 'home.html', context)

    return html_page


def elon(request):
    return render(request, 'elon.html')


def mission(request, id):
    try:
        mission = get_object_or_404(Mission, pk=id)
        return render(request, 'mission_details.html', {'mission': mission})
    except Http404:
        return render(request, '404.html')
        

def tesla(request):
    return redirect("http://tesla.com")


def astronauts(request):
    return render(request, 'astronauts.html', {'astronauts': Astro.objects.all()})


def add_astro(request):

    if request.method == "GET":
        myform = AddAstroForm()
        return render(request, 'add_astro.html', {'myform':myform})

    if request.method == "POST":

        myform = AddAstroForm(request.POST)

        if myform.is_valid():
            first_name=myform.cleaned_data['first_name']
            last_name=myform.cleaned_data['last_name']
            age=myform.cleaned_data['age']
            rank=myform.cleaned_data['rank']
            
            a1 = Astro(first_name=first_name, last_name=last_name, age=age, rank=rank)
            a1.save()

            return redirect('astronauts')

        else:
            return render(request, 'add_astro.html', {'myform':myform})


    