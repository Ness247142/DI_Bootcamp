from django.shortcuts import render
from django.http import HttpResponse
import json

with open("animal.json") as f:
    data = json.load(f)


def family(request, fam_id):
    fam_list = data['families']
    context = {}
    for fam in fam_list:
        if fam_id == fam['id']:
            context['name'] = fam['name']

    context['animals'] = []
    for fam_animal in data['animals']:
        if fam_animal['family'] == fam_id:
            context['animals'].append(fam_animal)

    html_page = render(request, 'family.html', context)
    return html_page


def animal(request, anim_id):

    animal_list = data['animals']
    context = {}

    context['animals'] = []
    for my_animal in animal_list:
        if my_animal['id'] == anim_id:
            context['animals'].append(my_animal)

    html_page = render(request, 'animal.html', context)
    return html_page



#Jonathan's solution
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

