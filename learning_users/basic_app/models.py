from django.db import models
from django.contrib.auth.models import User
from django import forms
from multiselectfield import MultiSelectField
from PIL import Image

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True, default="media/profile_pics/harry.jpeg")
    phone = models.CharField(max_length=200, default="+46 000 000 0000", blank=True)

    description = models.TextField(max_length=500, default="Profile Statement", blank=True)
    Checkbox_Choices = (('Python', 'Python'), ('javascript', 'javascript'),
                        ('React', 'React'), ('MySQL', 'MySQL'))
    courses = MultiSelectField(max_length=200, choices=Checkbox_Choices, default="courses")

    def __str__(self):
        return self.user.username

    def save(self):
        super().save()
        
        img = Image.open(self.profile_pic.path)

        if img.height > 200 or img.width > 200:
            output_size = (200,200)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

class SubscriberInfo(models.Model):
    subscriber_email = models.EmailField(null=True, blank=True, max_length=200, unique=True)

    def __str__(self):
        return self.subscriber_email


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
