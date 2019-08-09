from django.urls import path

from . import views

app_name = 'howdy'
urlpatterns = [
    path('', views.index, name='index'),
    path('api/exp/', views.ExperienceListCreate.as_view()),
    path('api/exp/<int:pk>/delete/', views.ExperienceDelete.as_view()),
    path('api/exp/pics', views.PictureDisplay.as_view()),
    path('api/exp/datainit', views.DataInitialization.as_view()),
    path('api/exp/<pk>/pred', views.SalaryPrediction),
    # path('api/exp/pred', views.SalaryPrediction),

]
