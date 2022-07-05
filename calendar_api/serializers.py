import datetime

from rest_framework import serializers
from .models import ConferenceRoom, Event


class ConferenceRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConferenceRoom
        fields = ('name', 'manager', 'address', 'events')


class EventSerializer(serializers.ModelSerializer):
    location = ConferenceRoomSerializer(read_only=True)

    def validate(self, data):
        time_diff = (data['end'] - data['start']).total_seconds()
        if time_diff / 60 > 480:
            raise serializers.ValidationError('Meeting cannot last longer than 8 hours')
        time_now = datetime.datetime.now(datetime.timezone.utc)
        if data['start'] < time_now:
            raise serializers.ValidationError('Meeting cannot start in the past')
        if data['end'] < data['start']:
            raise serializers.ValidationError('Meeting end date cannot be before start date')
        return data

    class Meta:
        model = Event
        fields = ('owner', 'title', 'meeting_agenda', 'start', 'end', 'location')
