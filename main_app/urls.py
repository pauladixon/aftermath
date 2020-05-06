from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('challenges/', views.challenges_index, name='challenges_index'),
    path('challenges/<int:challenge_id>/', views.challenges_detail, name='challenges_detail'),
    path('challenges/<int:challenge_id>/challenge_add_comment/', views.challenge_add_comment, name='challenge_add_comment'),
    path('challenges/comment/<int:pk>/delete/', views.ChallengeCommentDelete.as_view(), name='challenge_delete_comment'),
    path('posts/', views.posts_index, name='posts_index'),
    path('posts/<int:post_id>/', views.posts_detail, name='posts_detail'),
    path('posts/create/', views.PostCreate.as_view(), name='posts_create'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='posts_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='posts_delete'),
    path('posts/<int:post_id>/post_add_comment/', views.post_add_comment, name='post_add_comment'),
    path('posts/comment/<int:pk>/delete/', views.PostCommentDelete.as_view(), name='post_delete_comment'),
    path('posts/<int:post_id>/assoc_category/<int:category_id>/', views.assoc_category, name='assoc_category'),
    path('posts/<int:post_id>/unassoc_catetory/<int:category_id>/', views.unassoc_category, name='unassoc_category'),
    path('categories/', views.CategoryList.as_view(), name='categories_index'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='categories_detail'),
    path('categories/create/', views.CategoryCreate.as_view(), name='categories_create'),
    path('accounts/signup/', views.signup, name='signup'),
]