from django import forms
from django.forms import ModelForm
from .models import PostComment

class PostCommentForm(ModelForm):
  class Meta:
    model = PostComment
    fields = ['content']