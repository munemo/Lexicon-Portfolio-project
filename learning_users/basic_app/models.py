from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    description = models.CharField(max_length=200, default="description", blank=False)
    

    def __str__(self):
        return self.user.username


class checkBox(models.Model):
     skills = models.CharField(max_length=100)
     