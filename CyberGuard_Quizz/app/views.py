from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseBadRequest

from .forms import ContactForm
from .models import Quiz, Actualite, Loi


# Create your views here.
# def home(request):
#     actualites = Actualite.objects.all()
#     lois = Loi.objects.all()
#
#     return render(request, 'app/home.html',{'actualite': actualites, 'lois': lois})

import random

def home(request):
    actualites = Actualite.objects.all()
    lois = Loi.objects.all()
    random_lois = random.sample(list(lois), min(len(lois), 10))  # Sélectionne aléatoirement 5 lois
    return render(request, 'app/home.html', {'actualite': actualites, 'lois': random_lois})

def all_lois(request):
    lois = Loi.objects.all()
    return render(request, 'app/quiz/all_lois.html', {'lois': lois})

def loi_detail(request, loi_id):
    loi = get_object_or_404(Loi, pk=loi_id)
    return render(request, 'app/quiz/loi_detail.html', {'loi': loi})


# def register(request):
#     return render(request, 'app/authentication/register.html')
#
#
# def login(request):
#     return render(request, 'app/authentication/login.html')



# def displayQuizz(request):
#     quizz = Quiz.objects.all()
#     return render(request, 'app/quiz/home.html', {'quizz': quizz})
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def displayQuizz(request):
    quiz_list = Quiz.objects.all()
    paginator = Paginator(quiz_list, 10)  # 10 quiz par page

    page = request.GET.get('page')
    try:
        quizzes = paginator.page(page)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, affichez la première page
        quizzes = paginator.page(1)
    except EmptyPage:
        # Si la page est en dehors de la plage, affichez la dernière page
        quizzes = paginator.page(paginator.num_pages)

    return render(request, 'app/quiz/home.html', {'quizzes': quizzes})



# def quiz_detail(request, quiz_id):
#     quiz = get_object_or_404(Quiz, id=quiz_id)
#     return render(request, 'app/quiz/quiz_detail.html', {'quiz': quiz})


# def quiz_detail(request, quiz_id):
#     quiz = get_object_or_404(Quiz, id=quiz_id)
#     questions = quiz.questions.all()
#
#     if request.method == 'POST':
#         score = 0
#         total_questions = 0
#         for question in questions:
#             user_answer = request.POST.get('question' + str(question.id))
#             if user_answer:
#                 total_questions += 1
#                 if int(user_answer) == question.reponse_correcte:
#                     score += 1
#         return JsonResponse({'score': score, 'total_questions': total_questions})
#
#     return render(request, 'app/quiz/quiz_detail.html', {'quiz': quiz, 'questions': questions})

from django.shortcuts import render, get_object_or_404
from .models import Quiz




from django.shortcuts import render, get_object_or_404
from random import sample
from .models import Quiz, Question

from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question
from random import sample

# def quiz_detail(request, quiz_id):
#     quiz = get_object_or_404(Quiz, id=quiz_id)
#     score = None
#     selected_questions = None
#
#     if request.method == 'POST':
#         if 'question_count' in request.POST:
#             question_count = int(request.POST.get('question_count'))
#             all_questions = quiz.questions.all()
#             selected_questions = sample(list(all_questions), min(question_count, len(all_questions)))
#         elif 'verify' in request.POST:
#             questions = quiz.questions.all()
#             score = calculate_score(request, questions)
#
#     return render(request, 'app/quiz/quiz_detail.html', {'quiz': quiz, 'selected_questions': selected_questions, 'score': score})

def quiz_detail(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    return render(request, 'app/quiz/quiz_detail.html', {'quiz': quiz})


def check_answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        selected_choice = request.POST.get('choice')
        if selected_choice:
            selected_choice = int(selected_choice)
            if selected_choice == question.reponse_correcte:
                messages.success(request, 'Bonne réponse!')
            else:
                messages.error(request, 'Mauvaise réponse!')
        else:
            messages.error(request, 'Veuillez sélectionner une réponse.')
    return redirect('quiz_detail', quiz_id=question.quiz.id)

# def calculate_score(request, questions):
#     score = 0
#     total_questions = len(questions)
#     for question in questions:
#         choice_id = int(request.POST.get(f'question{question.id}', 0))
#         if choice_id == question.reponse_correcte:
#             score += 1
#     return score, total_questions

# def show_correction(request):
#     # Code pour afficher les corrections et le score
#     return render(request, 'app/quiz/corrections.html')



# def show_correction(request):
#     if request.method == 'POST':
#         selected_question_ids = request.POST.getlist('selected_questions')
#         selected_questions = Question.objects.filter(id__in=selected_question_ids)
#         quiz_id = int(request.POST.get('quiz_id'))
#         quiz = get_object_or_404(Quiz, id=quiz_id)
#         # Calculer le score
#         score = calculate_score(request, selected_questions)
#         # Rendre le gabarit de correction avec les données nécessaires
#         return render(request, 'app/quiz/corrections.html', {'quiz': quiz, 'score': score, 'selected_questions': selected_questions})
#     else:
#         # Rediriger vers la page d'accueil si la méthode de demande n'est pas POST
#         return redirect('home')


from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question

# def show_correction(request):
#     if request.method == 'POST':
#         selected_question_ids = request.POST.getlist('selected_questions')
#         quiz_id = request.POST.get('quiz_id')  # Récupérer l'ID du quiz depuis le formulaire
#         if quiz_id:
#             quiz = get_object_or_404(Quiz, id=quiz_id)
#             selected_questions = Question.objects.filter(id__in=selected_question_ids)
#             # Calculer le score
#             score = calculate_score(request, selected_questions)
#             # Rendre le gabarit de correction avec les données nécessaires
#             return render(request, 'app/quiz/corrections.html', {'quiz': quiz, 'score': score, 'selected_questions': selected_questions})
#         else:
#             # Rediriger vers la page d'accueil si l'ID du quiz est manquant
#             return redirect('home')
#     else:
#         # Rediriger vers la page d'accueil si la méthode de demande n'est pas POST
#         return redirect('home')
from django.shortcuts import render
from .models import Question



def show_correction(request):
    if request.method == 'POST':
        quiz_id = request.POST.get('quiz_id')
        questions = Question.objects.filter(quiz_id=quiz_id)
        score, corrections = calculate_score_and_corrections(request, questions)
        context = {'score': score, 'corrections': corrections}
        return render(request, 'app/quiz/corrections.html', context)
    else:
        return JsonResponse({'error': 'Invalid request'})

def calculate_score_and_corrections(request, questions):
    score = 0
    total_questions = len(questions)
    corrections = []

    for question in questions:
        choice_id = int(request.POST.get(f'question{question.id}', 0))
        if choice_id == question.reponse_correcte:
            score += 1
            corrections.append({'question': question.enonce, 'selected_choice': choice_id, 'correct_choice': question.reponse_correcte})
        else:
            corrections.append({'question': question.enonce, 'selected_choice': choice_id, 'correct_choice': question.reponse_correcte})

    return score, total_questions, corrections






def contactUs(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                'CyberGuard ',
                message,
                email,
                ['lacapacitee@gmail.com', 'lacapacitee@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'app/contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'app/home.html', {'form': form})
