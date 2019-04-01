from django.db import models

class Experience(models.Model):
    id = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)

