from django.db import models


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.question_text


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text

class Experience(models.Model):
    years = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)

#   class Meta:
#           ordering = ('country',) # helps in alphabetical listing. Sould be a tuple

#   def __str__(self):
#     return self.country+" : "+self.continent



# class News(models.Model):
#     news_title = models.CharField(max_length=200)
#     news_link = models.CharField(max_length=100)
#     news_date = models.DateField()
#     news_country = models.ManyToManyField(Country)  

#     def __str__(self):
#         return self.news_title