from django.db import models

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    aadhar_number = models.IntegerField()
    roll_number = models.IntegerField()
    address = models.CharField(max_length=50)
    exam_center = models.CharField(max_length=50)

    # Show object name to firstname
    def __str__(self):
        return self.firstname
