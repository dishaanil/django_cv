# Create your models here.
from django.db import models

class Experience(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Allow null for ongoing roles
    summary = models.TextField()

    def __str__(self):
        return f"{self.role} at {self.company}"

class Education(models.Model):
    name = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    marks = models.CharField(max_length=20)

    def __str__(self):
        return self.institution_name

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CV(models.Model):
    experiences = models.ManyToManyField(Experience)
    educations = models.ManyToManyField(Education)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return "CV"  # Optional, since the name field is no longer needed
