from django.db import models

# Create your models here.
class Teacher(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

class Student_E(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    age=models.IntegerField()
    classroom=models.CharField(max_length=100)
    teacher=models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

