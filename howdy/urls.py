from django.urls import path

from . import views

app_name = 'howdy'
urlpatterns = [
    path('', views.index, name='index'),
    path('data-add', views.data_add, name='data_add'),
    path('data-remove', views.data_remove, name='data_remove'),
    path('data-import', views.data_import, name='data_import'),
    path('data-predict', views.data_predict, name='data_predict')
]
