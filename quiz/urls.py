from django.urls import path, re_path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),#safe

    re_path(r'^records/(?P<slug>[\w-]+)/(?P<userid>\d+)/$', views.response_page, name='responses'),

    re_path(r'^question/(?P<slug>[\w-]+)/create/$', views.QuestionCreate.as_view(), name='question_create'),
    path('question/<int:pk>/update/', views.QuestionUpdate.as_view(), name='question_update'),#safe
    path('question/<int:pk>/delete/', views.QuestionDelete.as_view(), name='question_delete'),#safe

    re_path(r'^exam/(?P<slug>[\w-]+)/$', views.exam_view, name='exam'),#safe
    re_path(r'^qlist/(?P<slug>[\w-]+)/$', views.question_list, name='question_list'),#safe
]