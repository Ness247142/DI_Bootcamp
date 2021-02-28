from django.shortcuts import render
from django.http import HttpResponse

def people(request):
	return HttpResponse('people.sort(age)')

def people_id(request):
	return HttpResponse('people_id.sort')