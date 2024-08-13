from django.urls import path
from quizzes import views

urlpatterns = [
    path('', view=views.questions, name='questions'),
    path('topic/', views.topics, name='topics')
]