from django.db import models

#1 setting  Create your models here go to admin .

class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    city=models.CharField(max_length=100)
