from django.shortcuts import render, redirect
from basic_app.forms import UserForm, UserProfileInfoForm, SubscriberInfoForm, ContactForm
from basic_app.models import UserProfileInfo, SubscriberInfo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
import urllib.parse
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, send_mail, send_mass_mail, BadHeaderError
from django.conf import settings
from django.template.loader import render_to_string
from django.template import RequestContext
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,'basic_app/index.html')

@login_required
def portfoliopage(request):
    return render(request, "basic_app/portfolio_site.html")

@login_required
def list_profiles(request):
    profiles_list = UserProfileInfo.objects.order_by('user')
    profiles_dict = {'profiles':profiles_list}
    return render(request,'basic_app/list_profiles.html',context=profiles_dict)


@login_required
def special(request):
    return HttpResponse("You are now logged in.")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'basic_app/registration.html',{'user_form':user_form,
    'profile_form':profile_form,
    'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
             login(request,user)
             return portfoliopage(request)
            else:
               return HttpResponse("Account not found")
        else:
          print("Someone tried to login and failed.")
          print("Username: {} and password  {}".format(username,password))
          return HttpResponse("Login failed. Check username and password.")
    else:
        ## Kash added me (included the user_login_form variable/class for easy access in html)
        user_login_form = AuthenticationForm()
        return render(request,'basic_app/login.html',{'user_login_form':user_login_form})

def subscribe(request):
    subscribed = False
    if request.method == 'POST':
        subscriber_form = SubscriberInfoForm(data=request.POST)
        if subscriber_form.is_valid():
            subscriber = subscriber_form.save(commit=False)
            subscriber.save()
            print(subscriber)
            subscribed = True

            # send welcome email
            # change the dummy@testemail.com
            email = EmailMessage(
                'Welcome to Lex Job App',
                'Thank you for your subscription! Check your mailbox regularly for the hottest jobs in the tech field!',
                'settings.EMAIL_HOST_USER',
                ['dummy@testemail.com'], )
            email.fail_silenty = False
            email.send()

        else:
            print(subscriber_form.errors)
    else:
        subscriber_form = SubscriberInfoForm()

    return render(request, 'basic_app/subscribe.html',
    {'subscriber_form': subscriber_form,
     'subscribed':subscribed})

def list_subscribers(request):
    subscribers_list = SubscriberInfo.objects.order_by('subscriber_email')
    subscribers_dict = {'subscribers':subscribers_list}

    # send mass email
    # change the dummy@testemail.com
    email = EmailMessage(
        'Hot Jobs Available!',
        'More than 50 Full Stack Engineers and IT Security analysts for ABC Branch Stockholm.',
        'settings.EMAIL_HOST_USER',
        ['dummy@testemail.com'])

    email.fail_silenty = False
    email.send()

    return render(request,'basic_app/list_subscribers.html',context=subscribers_dict)


## Kash added me
def contact(request):
    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Submitted.')
            return redirect('/contact')
    else:
        f = ContactForm()
    return render(request, 'basic_app/contact.html', {'contact_form': f})

def searchprofile(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(username__icontains=query)
            results = User.objects.filter(lookups).distinct()

            context = {'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'basic_app/search.html', context)

        else:
            return render(request, 'basic_app/search.html')

    else:
        return render(request, 'basic_app/search.html')
