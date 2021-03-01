from django.shortcuts import render
from django.http import HttpResponse

def animal(request):
	return HttpResponse('{"animals": [{"id": 1, "name": "Dog", "legs": 4, "weight": 5.67, "height": 4.2, "speed": 34, "family": 2}, {"id": 2, "name": "Domestic Cat", "legs": 4, "weight": 5.67, "height": 4.2, "speed": 34, "family": 1}, {"id": 3, "name": "Panther", "legs": 4, "weight": 5.67, "height": 4.2, "speed": 34, "family": 1}, {"id": 4, "name": "Bears", "legs": 4, "weight": 5.67, "height": 4.2, "speed": 34, "family": 3}, {"id": 5, "name": "Snake", "legs": 0, "weight": 5.67, "height": 4.2, "speed": 34, "family": 4}, {"id": 6, "name": "Ant", "legs": 6, "weight": 5.67, "height": 4.2, "speed": 34, "family": 5}, {"id": 7, "name": "Spider", "legs": 8, "weight": 5.67, "height": 4.2, "speed": 34, "family": 6}, {"id": 8, "name": "Salamander", "legs": 4, "weight": 5.67, "height": 4.2, "speed": 34, "family": 7}]')

def family(request):
	return HttpResponse('{"families": [{"id": 1, "name": "Felidae"}, {"id": 2, "name": "Caninae"}, {"id": 3, "name": "Mammal"}, {"id": 4, "name": "Reptile"}, {"id": 5, "name": "Insect"}, {"id": 6, "name": "Arachnid"}, {"id": 7, "name": "Amphibian"}]')