from django.db import models
from django import forms
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics',blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    description = models.CharField(max_length=200, default="description", blank=False)
    
    Checkbox_Choices = (('Python', 'Python'),('javascript','javascript'),
                    ('React','React'), ('MySQL','MySQL'))
    courses = MultiSelectField(max_length=200, choices=Checkbox_Choices, default="courses")

    def __str__(self):
        return self.user.username

class SubscriberInfo(models.Model):
    subscriber_email = models.EmailField(null=True, blank=True, max_length=200, unique=True)

    def __repr__ (self):
        return '<SubscriberInfo %s>' % self.subscriber_email

## Kash added me
class Contact(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender")
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contact"

    def __str__(self):
        return self.name + "-" +  self.email
