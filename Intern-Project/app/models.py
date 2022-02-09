import email
from email import message
from turtle import home
from django.db import models
from datetime import datetime


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    surename = models.CharField(max_length=100)
    sex = models.CharField(max_length=50)
    dob = models.DateField(auto_now_add=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)
    image = models.ImageField(upload_to='home/userpic')

    def __str__(self) -> str:
        return self.name

# Contact-us
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self) -> str:
        return self.email