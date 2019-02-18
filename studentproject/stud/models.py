from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, blank=True)
    father_name = models.CharField(max_length=100, blank=True)
    mather_name = models.CharField(max_length=100, blank=True)
    address= models.TextField()
    dob= models.DateField( auto_now_add=True)
    age= models.IntegerField(default=0)
    _class=models.IntegerField(default=0)
    Speaks_Kannada = models.BooleanField(default=False)
    
