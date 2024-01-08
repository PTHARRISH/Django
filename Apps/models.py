from django.db import models

# Create your models here.
class student(models.Model): # models.Model is django models is a class and Model is a subclass
    firstname=models.CharField(max_length=100)
    
