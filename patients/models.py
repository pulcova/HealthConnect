from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Patient(models.Model):
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}" 
    
class Doctor(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)   
    
    def __str__(self):
        return self.user.email 