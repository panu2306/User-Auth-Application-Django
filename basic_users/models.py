from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    # create relationship with User Model(Don't inherit User Model)
    user = models.OneToOneField(User)

    # Add additional attributes you want 
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return self.user.username
    