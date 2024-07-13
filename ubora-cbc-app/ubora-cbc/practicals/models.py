from django.db import models
from teacher.models import Teacher_details

# Create your models here.

class Practicals(models.Model):
    id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=50)
    teacher_id = models.ForeignKey(Teacher_details, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.category_name}"