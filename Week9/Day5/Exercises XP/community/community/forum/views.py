from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages


def home(request):
    return render(request, 'index.html')


def posts(request):
    context = {
        'user': person,
        'page_title': "Posts",
        'posts': Post.objects.filter(
            author__first_name=person.first_name,
            author__last_name=person.last_name)
    }

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_to_add = form.save()
            for attr, value in post_to_add.__dict__.items():
                print(f'{attr} : {value}')

            return render(request, 'posts.html', context)
        else:
            print("---ERRORS---", form.errors)
            context['form'] = form
            return render(request, 'posts.html', context)

    else:
        context['form'] = PostForm()
    return render(request, 'posts.html', context)


class PostIndex(ListView):
    template_name = 'posts.html'
    context_object_name = 'posts'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostIndex, self).get_context_data(**kwargs)
        context['page_title'] = "Post"
        # context['user'] = person
        return context


class PostCreateIndex(CreateView):
    template_name = 'thread.html'
    form_class = PostForm

    def form_valid(self, form):
        post_to_add = form.cleaned_data
        print(post_to_add)
        return super().form_valid(form)
