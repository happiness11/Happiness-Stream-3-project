from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Sell(models.Model):
    """
    Here we'll define our Sell model
    """

    # author is linked to a registered
    # user in the 'auth_user' table.
    
    seller = models.ForeignKey('auth.User')
    car_name = models.CharField(max_length=200)
    car_model = models.CharField(max_length=200)
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    
    def __str__(self):
        return self.car_name
    
    def publish(self):
            self.published_date = timezone.now()
            self.save()