from django.urls import path

from . import views

app_name = 'howdy'
urlpatterns = [
    path('', views.index, name='index'),
    path('api/exp/', views.ExperienceListCreate.as_view()),
    path('api/exp/<int:pk>/delete/', views.ExperienceDelete.as_view()),
    path('api/exp/pics', views.PictureDisplay.as_view()),
    path('api/exp/datainit', views.MyView.as_view()),
]

# # urls.py
# urlpatterns = [
#     url(r'^myview/$', MyView.as_view()),
#     ...
# ]