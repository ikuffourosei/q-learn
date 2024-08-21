from django.urls import path
from quizzes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/login/', views.login_check, name='login'),
    path('quiz/logout/', views.logout_check, name='logout'),
    path('quiz/register/', views.register, name='register'),
    path('quiz/<str:topic_name>/', views.view_questions, name='questions'),
    path('quiz/<str:topic_name>/submit/', views.submit_quiz, name='submit'),
    path('quiz/<str:topic_name>/results/', views.result, name='results'),
    path('quiz/about', views.about, name='about'),
]
