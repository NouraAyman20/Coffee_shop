from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Coffee(models.Model):
  name=models.CharField(max_length=50)
  price=models.FloatField()  
  image =models.CharField(max_length=2083)
  
  def __str__(self):
      return self.name
  
  

class Add(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    quantity = models.IntegerField()  
    card_number = models.CharField(max_length=19)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    
    