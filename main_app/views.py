from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Challenge, Post, PostComment
from .forms import PostCommentForm



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')    

@login_required
def challenges_index(request):
    challenges = Challenge.objects.all()
    return render(request, 'challenges/index.html', {'challenges': challenges})

@login_required
def posts_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})

@login_required
def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    post_comment_form = PostCommentForm()
    return render(request, 
        'posts/detail.html', { 
            'post': post,
            'post_comment_form': post_comment_form,
            'user': request.user
        })


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'topic', 'content']

    def form_valid(self, form):
      form.instance.user = self.request.user  
      return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['topic', 'content']

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/posts/'

@login_required
def post_add_comment(request, post_id):
    form = PostCommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.post_id = post_id 
        new_comment.user_id = request.user.id 
        new_comment.save()
    return redirect('posts_detail', post_id=post_id)

class PostCommentDelete(LoginRequiredMixin, DeleteView):
    model = PostComment
    success_url = '/posts/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again' 
    form = UserCreationForm()
    context = { 'form': form, 'error_message': error_message} 
    return render(request, 'registration/signup.html', context)      


           
