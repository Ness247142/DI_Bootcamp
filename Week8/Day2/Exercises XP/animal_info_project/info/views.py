from django.shortcuts import render
import json


def all_animals(request):
    return render(request, 'animals_info.py', get_animals_data())


def single_animal(request, id):
    data = get_animals_data()
    if id > 0 and id <= len(data['animals']):
        single_animal = data['animals'][id - 1]
        return render(request, 'animal.html', {'animal': single_animal})


def get_animals_data():
    with open('animals.json', 'r') as f:
        data = json.load(f)
    return data


def family(request, id):
    pass


def animal(request, id):
    pass


def animals(request):
    f = open("animals_info.py", "r")
    print(f.read())
