from django.db import models


# Create your models here.
class students(models.Model): # models.Model is django models is a class and Model is a subclass
    firstname=models.CharField(max_length=100)
    start_date=models.DateField()
    end_date=models.DateField()
    comments=models.CharField(max_length=500,blank=True,null=True) # blank is True because it is not manditory field
    status=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname