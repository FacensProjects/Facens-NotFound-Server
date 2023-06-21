from django.conf import settings
from django.db import models
from datetime import datetime, time, timedelta
from typing import Tuple
# Create your models here.

class Student(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	user       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	ra         = models.CharField(max_length=10)

	def __str__(self):
		return self.user.first_name + " " + self.user.last_name

class Teacher(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	user       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	cpf        = models.CharField(max_length=11,blank=True,null=True)

	def __str__(self):
		return self.user.first_name + " " + self.user.last_name

class Course(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	name        = models.CharField(max_length=25)
	description = models.TextField(blank=True,null=True)

	def __str__(self):
		return self.name

class Region(models.Model):
	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at  = models.DateTimeField(auto_now=True)

	name        = models.CharField(max_length=10)

	def __str__(self):
		return self.name

class ClassLocation(models.Model):
	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at  = models.DateTimeField(auto_now=True)

	region      = models.ForeignKey(Region, on_delete=models.CASCADE)
	name        = models.CharField(max_length=10)

	def __str__(self):
		return self.name

class Class(models.Model):
	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at  = models.DateTimeField(auto_now=True)

	name        = models.CharField(max_length=25)
	description = models.TextField(blank=True,null=True)

	weekday_options = (
		('1', 'Domingo'),
		('2', 'Segunda'),
		('3', 'Terca'),
		('4', 'Quarta'),
		('5', 'Quinta'),
		('6', 'Sexta'),
		('7', 'Sabado'),
	)

	teacher     = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	course      = models.ForeignKey(Course, on_delete=models.CASCADE)
	location    = models.ForeignKey(ClassLocation, on_delete=models.CASCADE)
	weekday     = models.CharField(max_length=1,choices=weekday_options)
	time        = models.TimeField()
	duration    = models.DurationField(default=timedelta(minutes=50))
	
	def get_start(self):
		return self.time

	def get_end(self):
		duration_in_minutes = self.duration.total_seconds() / 60
		end_time = datetime.combine(datetime.min, self.time) + timedelta(minutes=duration_in_minutes)
		return end_time.time()

	def __str__(self):
		return self.name

class Notification(models.Model):
	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at  = models.DateTimeField(auto_now=True)

	title       = models.CharField(max_length=25)
	description = models.TextField()

	teacher   	= models.ForeignKey(Teacher, on_delete=models.CASCADE)
	course      = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True,null=True)

	date        = models.DateField()

	def __str__(self):
		return self.title

class StudentInscrition(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	student    = models.ForeignKey(Student, on_delete=models.CASCADE)
	course     = models.ForeignKey(Course, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.student)
