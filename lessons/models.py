from django.db import models

DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
)

WEEK_TYPES = (
    (0, 'Any_Week'),
    (1, 'Down_Week'),
    (2, 'Up_Week'),
)

LESSON_NUMBERS = (
    tuple((i, str(i)) for i in range(1, 10))
)


class DayOfWeek(models.Model):
    day_of_week = models.IntegerField(choices=DAYS_OF_WEEK, default=0)

    class Meta:
        unique_together = ('id', 'day_of_week')

    def __unicode__(self):
        return '%d: %s' % (self.id, self.day_of_week)

    def __str__(self):
        return str(dict(DAYS_OF_WEEK)[self.day_of_week])


class WeekType(models.Model):
    week_type = models.IntegerField(choices=WEEK_TYPES, default=0)

    def __str__(self):
        return str(dict(WEEK_TYPES)[self.week_type])


class Group(models.Model):
    group = models.CharField(max_length=5, default=0)

    def __str__(self):
        return self.group


class Lesson(models.Model):
    number = models.PositiveSmallIntegerField(choices=LESSON_NUMBERS, default=1)
    start_time = models.TimeField(default='00:00')
    end_time = models.TimeField(default='00:00')

    def __str__(self):
        return "#" + str(self.number) + " (" + str(self.start_time) + " | " + str(self.end_time) + ")"


class Discipline(models.Model):
    discipline = models.CharField(max_length=40, default=0)

    def __str__(self):
        return self.discipline


class LessonType(models.Model):
    lesson_type = models.CharField(max_length=10, default=0)

    def __str__(self):
        return self.lesson_type


class Audience(models.Model):
    audience = models.CharField(max_length=6, default=0)

    def __str__(self):
        return self.audience


class Schedule(models.Model):
    day_of_week = models.ForeignKey('DayOfWeek', default=0, on_delete=models.SET_DEFAULT)
    week_type = models.ForeignKey('WeekType', default=0, on_delete=models.SET_DEFAULT)
    lesson = models.ForeignKey('Lesson', default=0, on_delete=models.SET_DEFAULT)
    group = models.ForeignKey('Group', default=0, on_delete=models.SET_DEFAULT)
    discipline = models.ForeignKey('Discipline', default=0, on_delete=models.SET_DEFAULT)
    lesson_type = models.ForeignKey('LessonType', default=0, on_delete=models.SET_DEFAULT)
    audience = models.ForeignKey('Audience', default=0, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return str(self.day_of_week) + " " + str(self.lesson) + " " + str(self.group)
