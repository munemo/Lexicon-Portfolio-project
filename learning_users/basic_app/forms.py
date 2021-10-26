from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo, SubscriberInfo, Contact
from django.template.defaultfilters import slugify


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password','first_name','last_name')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic','phone','description','courses')

class SubscriberInfoForm(forms.ModelForm):
    class Meta():
        model = SubscriberInfo
        fields = ('subscriber_email',)

## Kash added me
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
