from rest_framework import viewsets
from lessons.models import Schedule
from .serializers import ScheduleSerializer


class ListSchedule(viewsets.ModelViewSet):
    queryset = Schedule.objects.all().order_by('day_of_week')
    serializer_class = ScheduleSerializer
