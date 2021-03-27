from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'projects'

urlpatterns = [
   
    path('', views.projects, name = 'projects'),
    path('<int:project_id>/', views.projectdetails, name = 'projectdetails')
  
]
