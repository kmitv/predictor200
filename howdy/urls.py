from django.urls import path

from . import views

app_name = 'howdy'
urlpatterns = [
    path('', views.index, name='index'),
    # path('data-add', views.wju.data_add, name='data_add'),
    # path('data-remove', views.wju.data_remove, name='data_remove'),
    # path('data-import', views.wju.data_import, name='data_import'),
    # path('data-predict', views.wju.data_predict, name='data_predict'),
    # path('', views.wju.as_view(), name='index'),
    path('api/exp/', views.ExperienceListCreate.as_view()),
    path('api/exp/delete', views.ExperienceDelete.as_view()),

    path('api/exp/<int:pk>/delete/', views.ExperienceDelete.as_view()),

]
