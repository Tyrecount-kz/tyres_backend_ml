from django.db import models

# Create your models here.
class Prediction(models.Model):
    city = models.CharField(max_length=200)
    year = models.CharField(max_length=10)
    shell = models.CharField(max_length=50)
    volume = models.CharField(max_length=50)
    mileage = models.CharField(max_length=30)
    transmisson = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    rudder = models.CharField(max_length=15)
    gear = models.CharField(max_length=35)
    custom_cleared = models.CharField(max_length=10)
    type_engine = models.CharField(max_length=10)
    company = models.CharField(max_length=150)

