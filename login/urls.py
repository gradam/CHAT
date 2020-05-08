from django.urls import path
from login import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register, name='register')
]