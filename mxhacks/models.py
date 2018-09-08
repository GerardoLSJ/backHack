from django.db import models
from django.contrib.postgres.fields import ArrayField

class Tags(models.Model):
	title = models.CharField(max_length=50, null=False, blank=False)
	description = models.CharField(max_length=255, null=False, blank=True)
	img = models.CharField(max_length=100, null=False, blank=False, default=" ")
	rating = models.IntegerField(null=False, blank=False, default=0)

class Procedure(models.Model):
	city = models.ForeignKey('City',on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=200)
	summary = models.CharField(max_length=1000)
	#steps = ArrayField(models.CharField(max_length=50), size=15)
	reference = models.CharField(max_length=100)
	tags = models.ManyToManyField('Tags')
	notes = models.CharField(max_length=1000)
	created = models.DateField(auto_now_add=True)
	update = models.DateField(auto_now=True,blank=True, null=True)
	rating = models.IntegerField(null=False, blank=False, default=0)

class Law(models.Model):
	city = models.ForeignKey('City',on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=200)
	summary = models.CharField(max_length=1000)
	#bullets = ArrayField(models.CharField(max_length=50), size=15)
	law = models.CharField(max_length=1000)
	reference = models.CharField(max_length=100)
	tags = models.ManyToManyField('Tags')
	notes = models.CharField(max_length=1000)
	created = models.DateField(auto_now_add=True)
	update = models.DateField(auto_now=True,blank=True, null=True)
	rating = models.IntegerField(null=False, blank=False, default=0)

class City(models.Model):
	name = models.CharField(max_length=50)
	country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)

class Country(models.Model):
	name = models.CharField(max_length=50)


