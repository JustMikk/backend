from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    platform = models.URLField()
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self) -> str:
        return self.name


class Announcement(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date = models.DateTimeField()

    def __str__(self) -> str:
        return self.name
