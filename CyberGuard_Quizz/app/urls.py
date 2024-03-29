from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path('lois/', views.all_lois, name='all_lois'),
    path('actualites/', views.all_actualites, name='all_actualites'),
    path('actualites/<int:pk>/', views.actualite_detail, name='actualite_detail'),
    path('ressources/', views.all_ressources, name='all_ressources'),
    path('ressources-pdf/', views.all_pdf_ressources, name='all_pdf_ressources'),
    path('loi/<int:loi_id>/', views.loi_detail, name='loi_detail'),
    # path("register/", views.register, name="register"),
    # path("login/", views.login, name="login"),
    path('quizz/', views.displayQuizz, name='display_quiz'),
    path('quiz_detail/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('show_correction/', views.show_correction, name='show_correction'),
    path('check_answer/<int:question_id>/', views.check_answer, name='check_answer'),
]


