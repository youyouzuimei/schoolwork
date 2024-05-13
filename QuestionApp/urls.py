from django.urls import path
from django.views.generic import RedirectView
from django.urls import re_path as url
from . import views

app_name = 'question'

urlpatterns = [
    path('question_index/<int:page_id>/', views.index, name='index'),
    path('<int:question_id>/', views.question_content, name="question_content"),
    path('add_question/', views.ask, name='add_question'),
    path('search/', views.search, name='search'),

    path('show_question/', views.questionContent, name='questionContent'),

    path('like-question/', views.like_question, name="like_question"),
    path('like/<int:id>/<str:action>/', views.like_question, name='like_question'),
    path('unlike/<int:id>/<str:action>/', views.like_question, name='like_question'),
    path('my_questions/', views.my_questions, name='my_questions'),
    path('redit-question/<int:question_id>/', views.redit_question, name="redit_question"),
    path('collect/<int:id>/<str:action>/', views.collect, name='collect_question'),
    path('collect/<int:id>/<str:action>/', views.collect, name='cancel_collect_question'),

    path('delete-question/<int:question_id>/', views.delete_question, name="delete_question"),
    
    path('my_center/',views.my_center,name='my_center'),
    path('my_answers/',views.my_answers,name='my_answers'),
]
