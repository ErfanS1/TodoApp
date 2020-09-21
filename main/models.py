from django.db import models
from django.utils import timezone
# Create your models here.

class Task(models.Model):
    text = models.CharField(max_length=200)
    added_time = models.DateTimeField(default=timezone.now)
    #remaining_days = models.IntegerField(default=1)
    status = models.CharField(max_length=50, default='Not Started')

    def __str__(self):
        return self.text+','+self.status
