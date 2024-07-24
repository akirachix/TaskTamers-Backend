from django.db import models
from student.models import Student_details
from assignments.models import Assignments


# Create your models here.

class Assignment_submission(models.Model):
    submission_id = models.IntegerField()
    student_id = models.ForeignKey(Student_details, on_delete = models.CASCADE)
    assignment_id = models.ForeignKey(Assignments, on_delete = models.CASCADE)
    grade = models.CharField(max_length = 10)

    def __str__(self):
        return f"{self.grade}"