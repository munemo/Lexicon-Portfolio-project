from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

class SubscriberInfo(models.Model):
    subscriber_email = models.EmailField(null=True, blank=True, max_length=200, unique=True)

    def __repr__ (self):
        return '<SubscriberInfo %s>' % self.subscriber_email



