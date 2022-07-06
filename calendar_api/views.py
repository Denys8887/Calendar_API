import pytz
from django.utils import timezone

from rest_framework import generics, mixins, filters
from rest_framework.permissions import IsAuthenticated

from .filters import IsOwnerFilterBackend
from .models import ConferenceRoom, Event
from .serializers import ConferenceRoomSerializer, EventSerializer


class TimezoneMixin:
    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        tzname = None
        if request.user.is_authenticated:
            tzname = request.user.timezone
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()


class ConferenceRoomList(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,):
    serializer_class = ConferenceRoomSerializer
    queryset = ConferenceRoom.objects.all()
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)


class CalendarEvent(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin,
                    mixins.RetrieveModelMixin, TimezoneMixin, ):
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Event.objects.all()
    filter_backends = (IsOwnerFilterBackend, filters.SearchFilter)
    search_fields = ['start', 'end', 'meeting_agenda', 'title']
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)
