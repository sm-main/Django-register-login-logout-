from django.shortcuts import render
from .models import *
from django.core.context_processors import csrf
from adddata.forms import *
from django.http import HttpResponseRedirect



def add_dinner(request):
	if request.method=='POST':
		form=DinnerForm(request.POST)
		if form.is_valid():
			name=form.cleaned_data['name']
			text=form.cleaned_data['text']
			query=Dinner(name=name,text=text)
			query.save()
			return HttpResponseRedirect('/thanks')
	else:
		form=DinnerForm()		
	return render(request,'home.html',{'form':form})

def thanks(request):
	return render(request,'thanks.html')


