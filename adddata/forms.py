from django import forms
class DinnerForm(forms.Form):
	name=forms.CharField(max_length=100)
	text=forms.CharField(max_length=255)
	
	