from django.db import models


class ChatMessage(models.Model):
    room = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.room

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'


class TemporaryUser(models.Model):
    username = models.CharField(max_length=20)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'username'
        verbose_name_plural = 'usernames'
