from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path('quizz/', views.displayQuizz, name='display_quiz'),
    path('quiz_detail/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
]
