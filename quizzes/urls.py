from django.urls import path
from quizzes import views

app_name = "quizzes"

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:topic_name>/', view=views.view_questions, name='questions'),
    path('<str:topic_name>/submit/', views.submit_quiz, name='submit'),
    path('<str:topic_name>/results/', views.result, name='results'),
    path('login/', views.login_check, name='login'),
    path('logout/', views.logout_check, name='logout'),
    path('register/', views.register, name='register'),
]