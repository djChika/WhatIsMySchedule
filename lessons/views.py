from django.shortcuts import render
from .models import Schedule


def schedule(request):
    schedule = Schedule.objects.all().order_by('day_of_week')
    return render(request, 'lessons/schedule.html', {'schedule': schedule})
