from .views import ConferenceRoomList, CalendarEvent
from django.urls import path

urlpatterns = [
    path('rooms/', ConferenceRoomList.as_view(), name='rooms'),
    path('rooms/<int:id>/', ConferenceRoomList.as_view(), name='room_details'),
    path('event/', CalendarEvent.as_view(), name='events'),
    path('event/<int:id>/', CalendarEvent.as_view(), name='event_details'),
]
