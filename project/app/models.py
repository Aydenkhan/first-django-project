from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Adil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    father = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    
