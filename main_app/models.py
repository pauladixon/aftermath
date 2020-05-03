from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Challenge(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('posts_detail', kwargs={'post_id': self.id})    