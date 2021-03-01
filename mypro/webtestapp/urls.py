# urls for application "webtestapp" only

from django.urls import path
from . import views

app_name='webtestapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('info', views.info, name='info'),
]

