from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone as _timezone


class ConferenceRoom(models.Model):
    """
    Stores info about calendars
    """
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manager')
    name = models.CharField(max_length=100)
    address = models.EmailField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    """
    Stores info about events
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    title = models.CharField(max_length=100)
    meeting_agenda = models.TextField()
    start = models.DateTimeField(default=_timezone.now)
    end = models.DateTimeField(default=_timezone.now)
    location = models.ForeignKey(ConferenceRoom, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['start']
