from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .models import Challenge, Post
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')    

def challenges_index(request):
    challenges = Challenge.objects.all()
    return render(request, 'challenges/index.html', {'challenges': challenges})

def posts_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})

class PostCreate(CreateView):
    model = Post
    fields = ['name']

    def form_valid(self, form):
      form.instance.user = self.request.user  
      return super().form_valid(form)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again' 
    form = UserCreationForm()
    context = { 'form': form, 'error_message': error_message} 
    return render(request, 'registration/signup.html', context)          
