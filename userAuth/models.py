from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user=models.OneToOneField(User)
	picture=models.ImageField(upload_to='userAuth/profilePics',blank=True)
	def __str__(self):
		return self.user.username

