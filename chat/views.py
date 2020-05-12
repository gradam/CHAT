from django.shortcuts import render


def index(request):
    return render(request, 'chat/index.html')


def room(response):

    username = response.user.username
    room_name = 'main'

    return render(response, 'chat/room.html', {
        'room_name': room_name,
        'username': username
    })
