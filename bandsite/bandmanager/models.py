from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Band(models.Model):
	name = models.CharField(max_length=100)
	website = models.CharField(max_length=200, blank=True)
	contact_info = models.CharField(max_length=200)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Member(models.Model):
	band = models.ForeignKey(Band, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	contact_info = models.CharField(max_length=200, blank=True)

	def __str__(self):
		 return self.name

@python_2_unicode_compatible
class Task(models.Model):
	band = models.ForeignKey(Band, on_delete=models.CASCADE)
	member = models.ForeignKey(Member)
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	difficulty = models.IntegerField(default=0)
	priority = models.IntegerField(default=0)

	def __str__(self):
		return self.title

@python_2_unicode_compatible
class Song(models.Model):
	band = models.ForeignKey(Band, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)

	def __str__(self):
		return self.title

@python_2_unicode_compatible
class Contact(models.Model):
	band = models.ForeignKey(Band)
	name = models.CharField(max_length=100)
	contact_info = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.name