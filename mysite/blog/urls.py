'''
Created on 2021. 3. 22.

@author: USER_L
'''
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from blog import views

urlpatterns = [
    
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    
    ]
