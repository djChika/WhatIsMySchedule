from rest_framework import serializers
from lessons import models as lesson_models
from lessons import models as frontend_models


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'group',
            'day',
            'time',
        )
        model = lesson_models.Lesson


class ScheduleSerializer(serializers.ModelSerializer):
    day_of_week = serializers.CharField(read_only=True)
    week_type = serializers.CharField(read_only=True)
    lesson = serializers.CharField(read_only=True)
    group = serializers.CharField(read_only=True)
    discipline = serializers.CharField(read_only=True)
    lesson_type = serializers.CharField(read_only=True)
    audience = serializers.CharField(read_only=True)

    class Meta:
        fields = (
            'id',
            'day_of_week',
            'week_type',
            'lesson',
            'group',
            'discipline',
            'lesson_type',
            'audience',
        )
        model = frontend_models.Schedule
