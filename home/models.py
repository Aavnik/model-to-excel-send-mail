from django.db import models

# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_age = models.IntegerField()
    student_phoneno = models.CharField( max_length=14)
    student_address = models.CharField(max_length=100)
    student_email = models.CharField(max_length=100)
    
    def __str__(self):
        return self.student_name
    



class Emails(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)   
    def __str__(self):
        return self.Name
     









