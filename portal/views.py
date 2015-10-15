from django.shortcuts import render
from django import forms
from portal import models
from portal.forms import UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):

    regStatus = False

    if request.method == 'POST':
        #grab info from raw information
        profile_form=UserProfileForm(data=request.POST)

        if profile_form.is_valid():
            user=profile_form.save(commit=False)

            #hash the password for security using the djangohash default method
            user.set_password(user.password)
            

            if 'profile_pic' in request.FILES:
                profile_pic = request.FILES['profile_pic']
            user.save()

            regStatus = True

        else:
            print profile_form.errors
    
    else:
        profile_form = UserProfileForm()
    
    return render(request, 'register.html', {'profile_form': profile_form, 'registered': regStatus})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect('/home/')
        else:
            return HttpResponse('Invalid login credentials')

    else:
        return render(request, 'login.html', {})

@login_required
def homepage(request):  

    return render(request, 'home.html', {})

@login_required
def AddStory(request):
    if request.method == 'POST':
        story = request.POST.get('ShoppingHistory')
        request.user.ShoppingHistory = story
        request.user.save()
        return render(request, 'ShoppingHistory.html', {'story': request.user})
    return render(request, 'ShoppingHistory.html', {})