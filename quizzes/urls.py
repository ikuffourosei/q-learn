from django.urls import path
from quizzes import views

app_name = "quizzes"

urlpatterns = [
    path('', views.index, name='index'),
    path('<topic_name>/', view=views.view_questions, name='questions'),
    path('<topic_name>/submit/', views.submit_quiz, name='submit'),
    path('<topic_name>/results/', views.result, name='results'),
    path('login/', views.login_check, name='login'),
    path('logout/', views.logout_check, name='logout'),
]