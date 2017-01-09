from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

# Create your models here.

@python_2_unicode_compatible
class Band(models.Model):
	name = models.CharField(max_length=100)
	website = models.CharField(max_length=200, blank=True)
	contact_info = models.CharField(max_length=200)
	picture_url = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.name


@python_2_unicode_compatible
class Member(models.Model):
	band = models.ForeignKey(Band, on_delete=models.CASCADE)
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=100)
	contact_info = models.CharField(max_length=200, blank=True)
	picture_url = models.CharField(max_length=200, blank=True)
	active = models.BooleanField(default=1)

	def __str__(self):
		return self.name

	#Whether member is active or not, inactive used for unassigned, for instance.
	def isActive(self):
    		return self.active


@python_2_unicode_compatible
class Task(models.Model):
	band = models.ForeignKey(Band, on_delete=models.CASCADE)
	member = models.ForeignKey(Member, null=True, blank=True)
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	difficulty = models.IntegerField(default=0)
	priority = models.IntegerField(default=0)

	def __str__(self):
		return self.title


@python_2_unicode_compatible
class TaskComment(models.Model):
	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	commenter = models.ForeignKey(Member, on_delete=models.CASCADE)
	body = models.CharField(max_length=500)

	def __str__(self):
		return self.body


@python_2_unicode_compatible
class Song(models.Model):
	band = models.ForeignKey(Band, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	progress = models.IntegerField(default=0)


	def __str__(self):
		return self.title


@python_2_unicode_compatible
class Contact(models.Model):
	band = models.ForeignKey(Band)
	name = models.CharField(max_length=100)
	contact_info = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.name