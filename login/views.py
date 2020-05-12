from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from login.models import Posts
from login.forms import CreatePost


def single_post(response, title):
    single_p = Posts.objects.get(title__iexact=title)
    if single_p in response.user.posts.all():
        return render(response, 'login/single_post.html', {'single_p': single_p})
    return render(response, 'login/home.html', {'single_p': single_p})


def profile_view(response):
    list_posts = Posts.objects.all()
    return render(response, 'login/profile.html', {'list_posts': list_posts})


def writing_post_view(response):
    if response.method == 'POST':
        form = CreatePost(response.POST)
        if form.is_valid():
            tit = form.cleaned_data['title']
            txt = form.cleaned_data['text']
            t = Posts(title=tit, text=txt)
            t.save()
            response.user.posts.add(t)
    else:
        form = Posts()

    return render(response, 'login/posts.html', {'form': form})


def home_view(response):

    if response.user.is_authenticated:
        log = f'Hello {response.user.username}'
    else:
        log = 'Welcome to ŁB please log in'

    return render(response, 'login/home.html', {'log': log})


def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = UserCreationForm()
    return render(response, 'login/register.html', {'form': form})
