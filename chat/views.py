from django.shortcuts import render


def index(request):
    return render(request, 'chat/index.html')


def room(response, room_name):

    username = response.user.username

    return render(response, 'chat/room.html', {
        'room_name': room_name,
        'username': username
    })
