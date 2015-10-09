from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    profile_pic = models.ImageField(upload_to='profile_images', blank=True)
    StaffMember = models.BooleanField(default=False)
    ShoppingHistory = models.TextField()
    ShoppingWishList = models.TextField()

    def __unicode__(self):
        return self.user.username
