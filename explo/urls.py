from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sans/result/', views.classifysoil, name='classifysoil'),
    path('sans/', views.sans, name='sans'),
    path('rakshit/', views.slopes, name='stabilityofslope'),
    path('mansi/', views.shear, name='shear'),
]