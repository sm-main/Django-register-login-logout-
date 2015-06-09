from django.db import models

class Dinner(models.Model):
	name=models.CharField(max_length=100)
	text=models.CharField(max_length=255)
	def __str__(self):
		return self.name
