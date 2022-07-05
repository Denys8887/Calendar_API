from django.contrib import admin

from calendar_api.models import ConferenceRoom, Event

admin.site.register(ConferenceRoom)
admin.site.register(Event)