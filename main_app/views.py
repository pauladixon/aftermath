from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Challenge, ChallengeComment, Post, PostComment, Category, Photo
from .forms import ChallengeCommentForm, PostCommentForm
import uuid
import boto3
import os

def some_function(request):
    my_key = os.environ['AWS_SECRET_ACCESS_KEY']

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'aftermath-bucket'

def home(request):
    challenges = Challenge.objects.all()
    posts = Post.objects.all()
    return render(request, 'home.html', {
        'challenges': challenges,
        'posts': posts
        })

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
    categories_posts_not_in = Category.objects.exclude(id__in = post.categories.all().values_list('id'))
    post_comment_form = PostCommentForm()
    return render(request, 'posts/detail.html', { 
        'post': post,
        'post_comment_form': post_comment_form,
        'categories': categories_posts_not_in,
        'user': request.user
    })

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
      form.instance.user = self.request.user  
      return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

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

@login_required
def add_photo(request, post_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, post_id=post_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('posts_detail', post_id=post_id)

class PostCommentDelete(LoginRequiredMixin, DeleteView):
    model = PostComment
    success_url = '/posts/'


@login_required
def challenges_detail(request, challenge_id):
    challenge = Challenge.objects.get(id=challenge_id)
    challenge_comment_form = ChallengeCommentForm()
    return render(request, 
        'challenges/detail.html', { 
            'challenge': challenge,
            'challenge_comment_form': challenge_comment_form,
            'user': request.user
        })

@login_required
def challenge_add_comment(request, challenge_id):
    form = ChallengeCommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.challenge_id = challenge_id 
        new_comment.user_id = request.user.id 
        new_comment.save()
    return redirect('challenges_detail', challenge_id=challenge_id)

class ChallengeCommentDelete(LoginRequiredMixin, DeleteView):
    model = ChallengeComment
    success_url = '/challenges/'

@login_required
def assoc_category(request, post_id, category_id):
    Post.objects.get(id=post_id).categories.add(category_id)
    return redirect('posts_detail', post_id=post_id)

@login_required
def unassoc_category(request, post_id, category_id):
    Post.objects.get(id=post_id).categories.remove(category_id)
    return redirect('posts_detail', post_id=post_id)

class CategoryList(LoginRequiredMixin, ListView):
    model = Category

class CategoryDetail(LoginRequiredMixin, DetailView):
    model = Category

class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = '__all__'

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


           
