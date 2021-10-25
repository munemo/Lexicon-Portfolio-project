from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm, SubscriberInfoForm
from basic_app.models import UserProfileInfo, SubscriberInfo
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, send_mass_mail, BadHeaderError
from django.template import RequestContext


# Create your views here.

def index(request):
    return render(request,'basic_app/index.html')

@login_required
def portfoliopage(request):
    return render(request, "basic_app/portfolio_site.html")

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
        return render(request,'basic_app/login.html',{})

def subscribe(request):
    subscribed = False
    if request.method == 'POST':
        subscriber_form = SubscriberInfoForm(data=request.POST)
        if subscriber_form.is_valid():
            subscriber = subscriber_form.save(commit=False)
            subscriber.save()
            subscribed = True
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
    print(subscribers_list)
    return render(request,'basic_app/list_subscribers.html',context=subscribers_dict)

#def welcome_subscribers(request):
#    # send welcome email
#    send_email('Welcome to Lexicon Job App!',
#              'Thank you for your subscription. We are glad to have you.',
#              'djangoprojectlex@gmail.com',
#              [''],
#              fail_silently=False
#              )
#    return render(request,'basic_app/index.html')


