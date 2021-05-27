from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


def add_gif(request):
    if request.method == 'POST':
        form = GifForm(request.POST)
        if form.is_valid():
            gif = Gif.objects.create(
                title=form.cleaned_data['title'],
                url=form.cleaned_data['url'],
                uploader_name=form.cleaned_data['uploader_name'],
            )
            for cat in form.cleaned_data['categories']:
                cat.gifs.add(gif)
            return redirect('view_gif', gif.id)
    return render(request, 'add_gif.html', {'form': GifForm()})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = Category.objects.create(
                name=form.cleaned_data['name'],
            )
            return redirect('view_categories')
    return render(request, 'add_category.html', {'form': CategoryForm()})


def view_gif(request, id):
    gif = get_object_or_404(Gif, pk=id)
    return render(request, 'show_gif.html', {'gif': gif})


def view_category(request, id):
    category = get_object_or_404(Category, pk=id)
    context = {
        'gif_list': category.gifs.all(),
        'page_title': f'{category.name} GIFs',
        'page_heading': f'all GIFs of the category {category.name}:'
    }
    return render(request, 'show_gifs.html', context)


def view_categories(request):
    cats = Category.objects.all()
    return render(request, 'show_categories.html', {'categories': cats})


def homepage(request):
    context = {
        'gif_list': Gif.objects.all(),
        'page_title': 'Homepage',
        'page_heading': 'Our GIFs'
    }
    return render(request, 'show_gifs.html', context)
