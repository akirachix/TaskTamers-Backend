from django.db import models
from practicals.models import Practicals
from practical_activities.models import Practical_activities

# Create your models here.

class Assignments(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)
    practical_id = models.ForeignKey(Practicals, on_delete = models.CASCADE)
    practical_activity_id = models.ForeignKey(Practical_activities, on_delete = models.CASCADE)
    release_date = models.DateField()
    due_date = models.DateField()

    def __str__(self):
        return f"{self.name}"