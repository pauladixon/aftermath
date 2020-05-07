from django import forms
from django.forms import ModelForm
from .models import PostComment, ChallengeComment, Category

class PostCommentForm(ModelForm):
  class Meta:
    model = PostComment
    fields = ['content']

class ChallengeCommentForm(ModelForm):
  class Meta:
    model = ChallengeComment
    fields = ['content']

class CategoryForm(ModelForm):
  class Meta:
    model = Category
    fields = ['name']