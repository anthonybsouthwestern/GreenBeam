from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

#All of this is from https://testdriven.io/blog/django-custom-user-model/


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
#Create table for the restaurant data or name Restuarants
class YelpOwned(models.Model):
    business_id = models.PositiveBigIntegerField(primary_key=1)
    name = models.TextField
    description = models.TextField
    yelp_rating = models.TextField
    phone_number = models.IntegerField(max_length=10)
    price = models.IntegerField(max_length=3)
    latitude = #figure out specific field
    longitude = #figure out specific field
    address = #figure out specific address and probably break this up into St number, street name, and city, state
    zip_code = models.IntegerField(max_length=5)
    image_url = #figure it out
    yelp_url = #figure it out
    
#class WeOwn(models.Model):
    
    