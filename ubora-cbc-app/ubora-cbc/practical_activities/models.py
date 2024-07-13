from django.db import models
from practicals.models import Practicals

# Create your models here.

class Practical_activities(models.Model):
    id = models.IntegerField(primary_key=True)
    activity_name = models.CharField(max_length=40)
    practical_id = models.ForeignKey(Practicals, on_delete = models.CASCADE)
    duration = models.CharField(max_length = 20)
    instruction = models.TextField()

    def __str__(self):
        return f"{self.activity_name}"