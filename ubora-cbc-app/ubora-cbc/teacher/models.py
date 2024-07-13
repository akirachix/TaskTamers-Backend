from django.db import models

# Create your models here.

class Teacher_details(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField()
    password = models.CharField(max_length = 12)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
