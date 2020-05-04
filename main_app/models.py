from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Challenge(models.Model):
    name = models.CharField(max_length=100)
    # add a class method
    # a model is just a class
    # you can write a class method to import data
    # the point is to call the api, grab 5 challenges, and save them to the database
    # then import the challenge model into the python repl shell and run that class method called import data 

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    topic = models.CharField(max_length=100, default='')
    content = models.TextField(max_length=250, default='')
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

   