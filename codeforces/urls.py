from django.urls import path, re_path
from . import views

app_name = 'problemset'

urlpatterns = [
    path('', views.pset, name='problemset'),
    re_path(r'^page/(?P<pg>\d+)/$', views.page, name='pages'),
    re_path(r'^problem/(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.forces_simplified, name='simpul'),
]