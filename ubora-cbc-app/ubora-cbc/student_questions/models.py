from django.db import models
from student.models import Student_details
# Create your models here.

class Student_questions(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.TextField()
    student_id = models.ForeignKey(Student_details, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.question}"