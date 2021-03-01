from django.shortcuts import render
from django.http import HttpResponse
import json

with open('animal.json') as f:
    data = json.load(f)

def family(request, families_id):
    family_list = data['animals']
    context = {}

    context['animals'] = []
    for an_animal in family_list:
        if an_animal['id'] == families_id:
            context['animals'].append(an_animal)

    html = render(request, 'family.html', context)
    return html

def animal(request, animals_id):
    animal_list = data['animals']
    context = {}

    for list_item in animal_list:
        if animals_id == list_item['id']:
            context['name'] = list_item['name']

    context['animals'] = []
    for animals in data['animals']:
        if animals['family'] == animals_id:
            context['animals'].append(animals)

    html = render(request, 'animal.html', context)
    return html


Jonathan's solution
from django.shortcuts import render
import json
def all_animals(request):
    return render(request, 'animals_list.html', get_animals_data())
def single_animal(request, id):
    data = get_animals_data()
    if id > 0 and id <= len(data['animals']):
        single_animal = data['animals'][id - 1]
        return render(request, 'animals_detail.html', {'animal': single_animal})
def get_animals_data():
    with open('animals.json', 'r') as f:
        data = json.load(f)
    return data
