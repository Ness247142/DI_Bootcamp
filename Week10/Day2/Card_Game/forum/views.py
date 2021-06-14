from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .urls import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def thread(request):

    if request.method == 'GET':
        return render(request,'thread.html',{'my_form':ThreadInputForm()})

    if request.method == 'POST':
        my_form = ThreadInputForm(request.POST)

        if my_form.is_valid():
            headline = my_form.cleaned_data['headline']
            subject = my_form.cleaned_data['subject']
            user = request.user
            Thread.objects.create(creator=user,headline=headline,subject=subject)
            return redirect('forum')  
        else:
            my_form = ThreadInputForm()
            return render(request,'thread.html',{'my_form':my_form})


def forum(request):

    if request.method == 'GET':
        return render (request,'forum.html',{'threads': Thread.objects.all()})


def single_thread(request, pk):

    if request.method == 'GET':
        thread = Thread.objects.get(id=pk)
        comment_form = CommentForm()
        context = {
            'thread':thread,
            'comment_form':comment_form
        }
        return render(request,'single_thread.html',context)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user_id = request.user
            comment.thread_id = Thread.objects.get(id=pk)
            comment.save()       
            return redirect('singlethread', pk) 
