from django.db import models

# Create your models here.
class admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class user_details(models.Model):
    Name = models.CharField(max_length=100)
    Dob = models.DateField()
    Gender = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)