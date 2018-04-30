from django.contrib import admin
from .models import DayOfWeek, WeekType, Group, Lesson, Discipline, LessonType, Audience, Schedule

admin.site.register(DayOfWeek)
admin.site.register(WeekType)
admin.site.register(Group)
admin.site.register(Lesson)
admin.site.register(Discipline)
admin.site.register(LessonType)
admin.site.register(Audience)
admin.site.register(Schedule)
