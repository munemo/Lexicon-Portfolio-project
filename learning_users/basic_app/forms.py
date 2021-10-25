from django import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo, SubscriberInfo 
from django.template.defaultfilters import slugify

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
     description = forms.CharField(widget=forms.Textarea())
     
     class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic', 'description' ,'courses')
        


class SubscriberInfoForm(forms.ModelForm):
    class Meta():
        model = SubscriberInfo
        fields = ('subscriber_email',)

## Kash added me
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

