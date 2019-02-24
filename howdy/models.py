from django.db import models

class Experience(models.Model):
    years = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)

