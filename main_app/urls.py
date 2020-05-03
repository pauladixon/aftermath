from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('challenges/', views.challenges_index, name='index'),
    path('challenges/<int:challenge_id>/', views.challenges_detail, name='detail'),
    path('free_forum/', views.free_forum_index, name='index'),
    path('free_forum/<int:free_forum_id>/', views.free_forum_detail, name='detail'),
]