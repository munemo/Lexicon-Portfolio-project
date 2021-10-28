from django import forms
from django.contrib.auth.models import User

from .models import UserProfileInfo, SubscriberInfo, Contact, MailJobList


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')


class UserProfileInfoForm(forms.ModelForm):

    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic', 'phone', 'description', 'courses')


class SubscriberInfoForm(forms.ModelForm):
    class Meta:
        model = SubscriberInfo
        fields = ['subscriber_email', ]


class MailJobListForm(forms.ModelForm):
    class Meta:
        model = MailJobList
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class ProfileUpdateForm(UserForm, ):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'phone', 'description', 'courses')
