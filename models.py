from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Student(models.Model):
    objects = None
    sales_person = models.ForeignKey(User, on_delete=models.CASCADE)
    joiningdate = models.DateField()
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    mobile = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    education = models.CharField(max_length=20)
    skills = models.CharField(max_length=100)

    def __str__(self):
        return self.name
