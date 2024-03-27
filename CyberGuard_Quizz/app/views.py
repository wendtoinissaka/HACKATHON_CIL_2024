from django.shortcuts import render, get_object_or_404

from .models import Quiz


# Create your views here.
def home(request):
    all = Quiz.objects.all()

    return render(request, 'app/home.html',{'quizz' :all})


def register(request):
    return render(request, 'app/authentication/register.html')


def login(request):
    return render(request, 'app/authentication/login.html')



def displayQuizz(request):
    quizz = Quiz.objects.all()
    return render(request, 'app/quiz/home.html', {'quizz': quizz})


def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'app/quiz/quiz_detail.html', {'quiz': quiz})
