from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
import random
# Create your models here.

class CustomeUser(AbstractUser):
    salary = models.IntegerField(null=True, blank=True)
    doj= models.DateField(null=True, blank=True)
    Department=models.CharField(null=True,blank=True,max_length=100)
    Designation=models.CharField(null=True,blank=True,max_length=500)
    Image=models.FileField(null=True,blank=True)
    
    
    def bg_color(self):
        # Generate a random pastel color
        return f"hsl({random.randint(0, 360)}, 70%, 80%)"

    
    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"
    def get_initials(self):
        # Generate initials based on first and last names
        first_letter = self.first_name[0].upper() if self.first_name else ""
        last_letter = self.last_name[0].upper() if self.last_name else ""
        return f"{first_letter}{last_letter}"
