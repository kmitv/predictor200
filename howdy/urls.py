from django.urls import path

from . import views

app_name = 'howdy'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('data-add', views.data_add, name='data_add'),
    path('data-remove', views.data_remove, name='data_remove')
]
