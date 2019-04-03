from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic

from django.views.generic import View
from rest_framework.views import APIView

import csv

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from howdy.models import Experience
from howdy.models import Picture
from howdy.serializers import ExperienceSerializer
from howdy.serializers import PictureSerializer

from rest_framework import generics

import requests

from django.http import HttpResponse

from rest_framework.renderers import JSONRenderer

from rest_framework.response import Response


def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')

def dataInit():
        post_list = [None] * Experience.objects.count()
        salary_list = [None] * Experience.objects.count()  

        exp_set = Experience.objects.filter(post__isnull=False)

        list_increment = 0

        for exp in exp_set:
                post_list[list_increment] = float(exp.post)
                salary_list[list_increment] = float(exp.salary)

                list_increment=list_increment+1

        global X
        global y

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

        global regressor

        regressor = LinearRegression()
        regressor.fit(X_train, y_train)

        # Fitting Polynomial Regression to the dataset
        from sklearn.preprocessing import PolynomialFeatures
        regressor = PolynomialFeatures(degree = 4)
        # regressor = PolynomialFeatures(degree = Experience.objects.count())
        X_poly = regressor.fit_transform(X)
        regressor.fit(X_poly, y)

        global poly_regressor

        poly_regressor = LinearRegression()
        poly_regressor.fit(X_poly, y)

        plt.clf()

        plt.scatter(X, y, color = 'red')
        plt.plot(np.sort(X, axis=0), poly_regressor.predict(regressor.fit_transform(np.sort(X, axis=0))), color = 'blue')
        plt.title('reg')
        plt.xlabel('level')
        plt.ylabel('Salary')
        plt.savefig('howdy/static/howdy/foo.png')

        print("ok")


class wju(View):

        
        # dataInit(self)

        def get(self, request, *args, **kwargs):
                self.dataInit()

                for i in range (101):
                        print(float(poly_regressor.predict(regressor.fit_transform(np.array([i/10]).reshape(-1, 1)))))

                experience_list = Experience.objects.all()
                context = {'experience_list': experience_list}
                return render(request, "index.html", context=context)

        def post(self, request, *args, **kwargs):
                if request.POST.get('post') and request.POST.get('salary'):
                        post=Experience()

                        worked= request.POST.get('worked')
                        averageTime= request.POST.get('averageTime')

                        post.post= int(request.POST.get('post')) + int(worked)/int(averageTime)
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
                        self.dataInit()

                        plt.clf()

                        plt.scatter(X, y, color = 'red')
                        plt.plot(np.sort(X, axis=0), poly_regressor.predict(regressor.fit_transform(np.sort(X, axis=0))), color = 'blue')
                        plt.title('reg')
                        plt.xlabel('level')
                        plt.ylabel('Salary')
                        plt.savefig('howdy/static/howdy/foo.png')

                        print(regressor)
                        print(poly_regressor)

                        return redirect('/')  

class ExperienceListCreate(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class PictureDisplay(generics.ListCreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class ExperienceDelete(generics.DestroyAPIView):
        serializer_class = ExperienceSerializer

        def get_queryset(self):
                queryset = Experience.objects.filter(id=self.kwargs['pk'])
                return queryset
        
        def destroy(self, request, *args, **kwargs):
                instance = self.get_object()
                self.perform_destroy(instance)
                return Response(status=204)

class MyView(APIView):
    def get(self, request, *args, **kwargs):
        dataInit()
        return Response(dataInit())

