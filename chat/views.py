from django.shortcuts import render


def index(request):
    return render(request)


def room(response):

    username = response.user.username
    room_name = 'main'

    return render(response, {
        'room_name': room_name,
        'username': username
    })
