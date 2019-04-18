from django.db import models
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your models here.
class School(models.Model):
	name = models.CharField(max_length=256)
	principal = models.CharField(max_length=256)
	location = models.CharField(max_length=256)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('CVB:detail', kwargs={'pk':self.pk})

class Student(models.Model):
	name = models.CharField(max_length=256)
	age = models.PositiveIntegerField()
	school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('CVB:detail', kwargs={'pk':self.school.pk})
