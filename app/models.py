from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomeUser(AbstractUser):
    salary = models.IntegerField(null=True, blank=True)
    doj= models.DateField(null=True, blank=True)
    Department=models.CharField(null=True,blank=True,max_length=100)
    Designation=models.CharField(null=True,blank=True,max_length=500)
    Image=models.FileField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='employee_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"