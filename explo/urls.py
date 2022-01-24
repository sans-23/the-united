from django.urls import path

from . import views

app_name = 'explo'

urlpatterns = [
    path('', views.home, name='home'),
    path('sans/result/', views.classifysoil, name='classifysoil'),
    path('sans/', views.sans, name='sans'),
]