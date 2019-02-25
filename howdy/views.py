#  # howdy/views.py
# from django.shortcuts import render
# from django.views.generic import TemplateView

# # Create your views here.
# class HomePageView(TemplateView):
#     def get(self, request, **kwargs):
#         return render(request, 'index.html', context=None)


from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic

import csv

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from howdy.models import Experience

class IndexView(generic.ListView):
        template_name = 'index.html'
        context_object_name = 'experience_list'

        def get_queryset(self):
                return Experience.objects.all()


def data_add(request):
        if request.method == 'POST':
                if request.POST.get('years') and request.POST.get('salary'):
                        

                        post=Experience()
                        post.years= request.POST.get('years')
                        post.salary= request.POST.get('salary')
                        post.save()
                        return redirect('/') 
        else:
                return redirect('/') 

def data_remove(request):
        if request.method == 'POST':
                if request.POST.get('index'):
                        to_del = Experience.objects.get(id = request.POST.get('index'))
                        to_del.delete()
                        return redirect('/') 
        else:
                return redirect('/') 

def data_import(request):

        if request.method == 'POST':
                if request.POST.get('import'):
                        years_list = [None] * Experience.objects.count()
                        salary_list = [None] * Experience.objects.count()  

                        exp_set = Experience.objects.filter(years__isnull=False)

                        list_increment = 0

                        for exp in exp_set:
                                years_list[list_increment] = float(exp.years)
                                salary_list[list_increment] = float(exp.salary)

                                list_increment=list_increment+1
                        
                        X = np.array(years_list)
                        y = np.array(salary_list)

                        from sklearn.model_selection import train_test_split
                        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
                        
                        from sklearn.linear_model import LinearRegression
                        regressor = LinearRegression()
                        regressor.fit(X_train.reshape(-1,1), y_train.reshape(-1,1))

                        # y_pred = regressor.predict(X_test.reshape(-1, 1))

                        print(regressor.predict(X_train.reshape(-1,1)))

                        plt.clf()

                        plt.scatter(X, y, color = 'red')
                        plt.plot(X_test, regressor.predict(X_test.reshape(-1,1)), color = 'blue')
                        plt.title('Salary vs Experience (Test set)')
                        plt.xlabel('Years of Experience')
                        plt.ylabel('Salary')
                        plt.savefig('howdy/static/howdy/foo.png')

                        return redirect('/') 
        return redirect('/') 

def data_predict(request):
        if request.method == 'POST':
                if request.POST.get('pred_query'):
                        query = request.POST.get('pred_query')
                        
                        return redirect('/') 
        else:
                return redirect('/') 
