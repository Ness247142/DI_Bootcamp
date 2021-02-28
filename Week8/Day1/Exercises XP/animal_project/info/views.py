from django.shortcuts import render  # this line is added automatically
from django.http import HttpResponse  # pass view information into the browser

with open('animal_info.json') as fl:
    data = json.load(fl)

def family(request, family_id):
	pass


def animals(request, animal_id):
	family_list = data['animals']
	context = {}

	for list_item in family_list:
		if animals_id == list_item['id']:
			context['name'] = list_item['name']

	context['animals'] = []
	for fam_animal in data['animals']:
		if fam_animal['family'] == animals_id:
			context['animals'].append(fam_animal)

	    html = render(request, 'animal.html', context)
	    return html
