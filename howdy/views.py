from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic

from django.views.generic import View

import csv

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from howdy.models import Experience

class wju(View):

        post_list = [None] * Experience.objects.count()
        salary_list = [None] * Experience.objects.count()  

        exp_set = Experience.objects.filter(post__isnull=False)

        list_increment = 0

        for exp in exp_set:
                post_list[list_increment] = float(exp.post)
                salary_list[list_increment] = float(exp.salary)

                list_increment=list_increment+1
                        
        X = np.array(post_list).reshape(-1,1)
        y = np.array(salary_list).reshape(-1,1)

        print(X)
        print(y)
                
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
                        
        print(X_train)
        print(y_train)

        # Fitting Linear Regression to the dataset
        from sklearn.linear_model import LinearRegression
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)

        # Fitting Polynomial Regression to the dataset
        from sklearn.preprocessing import PolynomialFeatures
        regressor = PolynomialFeatures(degree = Experience.objects.count())
        X_poly = regressor.fit_transform(X)
        regressor.fit(X_poly, y)
        poly_regressor = LinearRegression()
        poly_regressor.fit(X_poly, y)


        def get(self, request, *args, **kwargs):
                experience_list = Experience.objects.all()
                context = {'experience_list': experience_list}
                return render(request, "index.html", context=context)

        def post(self, request, *args, **kwargs):
                if request.POST.get('post') and request.POST.get('salary'):
                        post=Experience()
                        post.post= request.POST.get('post')
                        post.salary= request.POST.get('salary')
                        post.save()
                        return redirect('/') 
                
                if request.POST.get('index'):
                        to_del = Experience.objects.get(id = request.POST.get('index'))
                        to_del.delete()
                        return redirect('/')       

                if request.POST.get('index'):
                        to_del = Experience.objects.get(id = request.POST.get('index'))
                        to_del.delete()
                        return redirect('/')      

                if request.POST.get('import'):

                        plt.clf()

                        plt.scatter(self.X, self.y, color = 'red')
                        plt.plot(np.sort(self.X, axis=0), self.poly_regressor.predict(self.regressor.fit_transform(np.sort(self.X, axis=0))), color = 'blue')
                        plt.title('reg')
                        plt.xlabel('level')
                        plt.ylabel('Salary')
                        plt.savefig('howdy/static/howdy/foo.png')

                        print(self.regressor)
                        print(self.poly_regressor)

                        return redirect('/')  

                if request.POST.get('pred_query'):
                        query = float(request.POST.get('pred_query'))
                        pred = float(self.poly_regressor.predict(self.regressor.fit_transform(np.array([query]).reshape(-1, 1))))
                        context = {'experience_list': Experience.objects.all(), 'pred': pred}
                        return render(request, 'index.html', context)
