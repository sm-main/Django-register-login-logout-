from django.shortcuts import render
from userAuth.forms import *
from django.http import HttpResponseRedirect,HttpResponse
from .models import *
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth.decorators import login_required

def register(request):
	registered=False
	if request.method=='POST':
		user_form=UserForm(data=request.POST)
		profile_form=UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)
			user.save()
			profile=profile_form.save(commit=False)
			profile.user=user
			if 'picture' in request.FILES:
				profile.picture=request.FILES['picture']
			profile.save()
			registered=True
		else:
			print(user_form.errors,profile_form.errors)
	else:
		user_form=UserForm()
		profile_form=UserProfileForm()
	return render(request,'register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})
						 
def login(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(username=username,password=password)
		if user:
			if user.is_active:
				auth_login(request,user)
				return HttpResponseRedirect('/index/')
			else:
				return HttpResponse("Your acount is not active")
		else:
			print("invalid user details: {0} , {1}".format(username,password))
			return HttpResponse("invalid login details")
	else:
		return render(request,'login.html')		

def index(request):
	return render(request,'index.html')
@login_required	
def logOut(request):
	logout(request)
	return HttpResponseRedirect('/index/')


