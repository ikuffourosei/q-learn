from django.urls import path
from quizzes import views

urlpatterns = [
    path('<topic_name>/', view=views.questions, name='questions'),
]