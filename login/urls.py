from django.urls import path
from login import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register, name='register'),
    path('posts/', views.writing_post_view, name='posts'),
    path('profile', views.profile_view, name='profile'),
    path('posts/<str:title>', views.single_post, name='single_post')
]
