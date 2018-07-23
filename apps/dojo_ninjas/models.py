from __future__ import unicode_literals
from django.db import models

# Create your models here.
class dojos(models.Model):
	name = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=2)
	desc = models.CharField(max_length=1000, default='poopy')
	
class ninjas(models.Model):
	dojo = models.ForeignKey(dojos, related_name='location')
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)

class Book(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)