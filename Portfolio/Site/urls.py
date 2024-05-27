# Portfolio/urls.py

from . import views
from django.urls import path
from .views import index

urlpatterns = [
    path('index/',index,name='index'),
    path('project/',views.project,name='index'),
   
]