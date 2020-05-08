from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


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
