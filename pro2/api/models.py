from django.db import models

# Create your models here.
# this model is import on admin page 2 step 
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    city=models.CharField(max_length=100)