from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import datetime

CATEGORIES = (
    ('M', 'meetup'),
    ('P', 'python'),
    ('D', 'django'),
    ('Q', 'postgresql'),
    ('J', 'javascript'),
    ('N', 'node.js'),
    ('E', 'express'),
    ('G', 'mongodb'),
    ('H', 'html'),
    ('C', 'css'),
    ('O', 'other'),
)

class Challenge(models.Model):
    date = models.DateField(default=datetime.datetime.now)
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('challenges_detail', kwargs={'challenge_id': self.id})

class ChallengeComment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=200)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category
    
    def get_absolute_url(self):
        return reverse('categories_detail', kwargs={'pk': self.id})

class Post(models.Model):
    date = models.DateField(default=datetime.datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    topic = models.CharField(max_length=100, default='')
    content = models.TextField(max_length=250, default='')
    categories = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts_detail', kwargs={'post_id': self.id})

class PostComment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
