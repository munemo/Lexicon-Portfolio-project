from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm, SubscriberInfoForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from django.template import RequestContext

def index(request):
    return render(request,'basic_app/index.html')

def portfoliopage(request):
    return render(request, "basic_app/portfolio_site.html")

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
                profile.description = request.FILES['description']
                
         
              
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




