from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
class UserProfile(AbstractUser):
    
    #user = models.OneToOneField(User)

    profile_pic = models.ImageField(upload_to='profile_images', blank=True)
    StaffMember = models.BooleanField(default=False)
    ShoppingHistory = models.TextField(null=True)
    ShoppingWishList = models.TextField(null=True)

    def __unicode__(self):
        return self.username
