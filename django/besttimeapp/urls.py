# -*- coding: utf-8 -*-

from django.urls import path
from . import views

app_name = 'besttimeapp'

urlpatterns = [
    path(r'index/', views.index, name='index'),
    path(r'about/', views.about, name='about'), 
    path(r'info/', views.info, name='info'),
    path(r'signup/', views.signup, name='signup'),
    path(r'alldata/', views.get_alldata, name='alldata'),
    path(r'<str:name>/best/', views.get_best, name='best'),
]
