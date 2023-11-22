from django.db import models

# Create your models here.


class Event(models.Model):
    # image = models.ImageField(upload_to="/events", blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)  # Fix the typo here
    platform = models.URLField()
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self) -> str:
        return self.name
