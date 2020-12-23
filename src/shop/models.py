from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator,MinValueValidator

from rest_framework.reverse import reverse as api_reverse

from datetime import date

User = settings.AUTH_USER_MODEL

# Create your models here.
class Car(models.Model):
    user_id = models.ForeignKey(User, default=1, null=True,on_delete=models.CASCADE)
    car_model = models.CharField(max_length=150,null=True)
    release_year = models.DateField(blank=True,null=True)
    shell = models.CharField(max_length=150,null=True)
    mileage = models.IntegerField(blank=True,null=True)
    transmission = models.CharField(max_length=150,null=True)
    rudder = models.CharField(max_length=60,null=True)
    color = models.CharField(max_length=150,null=True)
    gear = models.CharField(max_length=150,null=True)
    custom_clear = models.CharField(max_length=150,null=True)
    price = models.CharField(max_length=150,null=True)
    engine_volume = models.CharField(max_length=150,null=True)
    city = models.CharField(max_length=250,null=True)
    views = models.IntegerField(default=0)
    added_to_wishlist = models.IntegerField(default=0,validators=[MaxValueValidator(1),MinValueValidator(0)])
    created_date = models.DateTimeField(auto_now_add=True)
    post_name = models.CharField(max_length=300,null=True)
    post_description = models.TextField(null=True)

    @property
    def owner(self):
        return self.user_id

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"

    def __str__(self):
        return self.car_model

    def get_api_detail_url(self):
        return api_reverse("api-cars:car-rud",kwargs={'pk':self.pk})

class Wishlist(models.Model):
    post_id = user_id = models.ForeignKey(Car, default=1,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, default=1, null=True,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)