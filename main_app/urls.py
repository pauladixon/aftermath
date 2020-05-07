from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('challenges/', views.challenges_index, name='challenges_index'),
    path('posts/', views.posts_index, name='posts_index'),
    path('posts/<int:post_id>/', views.posts_detail, name='posts_detail'),
    path('posts/create/', views.PostCreate.as_view(), name='posts_create'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='posts_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='posts_delete'),
    path('posts/<int:post_id>/post_add_comment/', views.post_add_comment, name='post_add_comment'),
    path('posts/comment/<int:pk>/delete/', views.PostCommentDelete.as_view(), name='post_delete_comment'),
    path('accounts/signup/', views.signup, name='signup'),
    path('posts/<int:post_id>/add_photo/', views.add_photo, name='add_photo'),
]