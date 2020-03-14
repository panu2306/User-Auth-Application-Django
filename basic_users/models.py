from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    # create relationship with User Model(Don't inherit User Model)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add additional attributes you want 
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
    