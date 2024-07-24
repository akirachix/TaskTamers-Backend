from django.db import models
from student_questions.models import Student_questions
from teacher.models import Teacher_details

# Create your models here.

class Teacher_answers(models.Model):
    id = models.IntegerField(primary_key=True)
    answer = models.TextField()
    question_id = models.ForeignKey(Student_questions, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher_details, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.answer}"