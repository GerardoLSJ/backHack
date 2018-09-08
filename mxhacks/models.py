from django.db import models
from django.contrib.postgres.fields import ArrayField

class Tags(models.Model):
	title = models.CharField(max_length=50, null=False, blank=False)
	description = models.CharField(max_length=255, null=False, blank=True)
	img = models.CharField(max_length=100, null=False, blank=False, default=" ")
	rating = models.IntegerField(null=False, blank=False, default=0)
	def __str__(self):
		return '%s' % (self.title)

class Procedure(models.Model):
	city = models.ForeignKey('City',on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=200)
	summary = models.CharField(max_length=1000)
	steps = models.TextField(max_length=1000, null=True,blank=False, default="")
	reference = models.CharField(max_length=100)
	tags = models.ManyToManyField('Tags')
	notes = models.CharField(max_length=1000)
	created = models.DateField(auto_now_add=True)
	update = models.DateField(auto_now=True,blank=True, null=True)
	rating = models.IntegerField(null=False, blank=False, default=0)
	def __str__(self):
		return '%s' % (self.title)

class Law(models.Model):
	city = models.ForeignKey('City',on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=200)
	summary = models.CharField(max_length=1000)
	bullets = models.TextField(max_length=1000, null=True,blank=False, default="")
	law = models.CharField(max_length=1000)
	reference = models.CharField(max_length=100,null=True,blank=True)
	tags = models.ManyToManyField('Tags')
	notes = models.CharField(max_length=1000)
	created = models.DateField(auto_now_add=True)
	update = models.DateField(auto_now=True,blank=True, null=True)
	rating = models.IntegerField(null=False, blank=False, default=0)
	def __str__(self):
		return '%s' % (self.title)

class City(models.Model):
	name = models.CharField(max_length=50)
	country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)
	def __str__(self):
		return '%s' % (self.name)
class Country(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return '%s' % (self.name)

