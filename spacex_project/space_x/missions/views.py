from django.shortcuts import render
from django.http import HttpResponse
from .models import Mission

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
