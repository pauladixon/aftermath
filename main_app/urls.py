from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('challenges/', views.challenges_index, name='index'),
    path('posts/', views.posts_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
]