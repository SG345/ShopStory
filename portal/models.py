from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
class UserProfile(AbstractUser):
    
    #user = models.OneToOneField(User)

    profile_pic = models.ImageField(upload_to='profile_images', blank=True)
    StaffMember = models.BooleanField(default=False)
    ShoppingHistory = models.TextField(null=True)
    ShoppingWishList = models.TextField(null=True)
    ItemsBought = models.ManyToManyField(Products)

    def __unicode__(self):
        return self.username

class Products(models.Model):
    product_title = models.TextField()
    product_type = models.TextField()
    product_link = models.TextField()
    product_image = models.ImageField(upload_to='product_images',blank=True)
    product_price = models.TextField(null=True)
    