from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def challenges_index(request):
    return render(request, 'challenges/index.html', {'challenges': challenges})

def challenges_detail(request):
    return render(request, 'challenges/detail.html', {'challenge': challenge})

def free_forum_index(request):
    return render(request, 'free_forum/index.html', {'free_forum': free_forum})

def free_forum_detail(request):
    return render(request, 'free_forum/detail.html', {'free_forum': free_forum})