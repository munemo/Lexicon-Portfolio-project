from django.db import models
from django.contrib.auth.models import User
from django import forms
from multiselectfield import MultiSelectField

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    phone = models.CharField(max_length=200, default="+46 000 000 0000", blank=True)

    description = models.TextField(max_length=500, default="Profile Statement", blank=True)
    Checkbox_Choices = (('Python', 'Python'), ('javascript', 'javascript'),
                        ('React', 'React'), ('MySQL', 'MySQL'))
    courses = MultiSelectField(max_length=200, choices=Checkbox_Choices, default="courses")

    def __str__(self):
        return self.user.username

class SubscriberInfo(models.Model):
    subscriber_email = models.EmailField(null=True, blank=True, max_length=200, unique=True)

    def __str__(self):
        return self.subscriber_email



