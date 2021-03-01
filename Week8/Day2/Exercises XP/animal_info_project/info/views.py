from django.shortcuts import render
from .models import Family, Animal

# Create your views here.
def family(request, family_id):
    family_info = Family.objects.get(id=family_id)
    animals = Animal.objects.filter(family=family_info)
    context = {
        'family': family_info,
        'animals': animals
        }
    return render(request, 'family.html', context)


def animal(request, animal_id):
    animals = Animal.objects.get(id=animal_id)
    context = {'animal': animal}
    return render(request, 'animal.html', context)


def animals(request):
    animals_all = Animal.objects.all()
    context = {'animals_all': animals_all}
    return render(request, 'animals.html', context)
