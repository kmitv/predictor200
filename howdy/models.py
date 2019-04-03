from django.db import models

class Experience(models.Model):
    post = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)

class Picture(models.Model):
    pic_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "howdy/static/howdy")