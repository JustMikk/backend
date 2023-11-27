from rest_framework import serializers
from .models import Event, Announcement


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'platform', 'start', 'end']
        read_only_fields = ['id']


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'name', 'description', 'date']
        read_only_fields = ['id']
