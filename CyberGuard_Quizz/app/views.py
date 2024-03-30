from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseBadRequest

from .forms import ContactForm, FuturePartenaireForm, SignalementForm
from .models import Quiz, Actualite, Loi, RessourceEducative, RessourcePdf, RessourceVideo, ConseilSecurite, Partenaire

# Create your views here.
# def home(request):
#     actualites = Actualite.objects.all()
#     lois = Loi.objects.all()
#
#     return render(request, 'app/home.html',{'actualite': actualites, 'lois': lois})

import random
from itertools import groupby  # Importez groupby depuis itertools
# def home(request):
#     actualites = Actualite.objects.all()
#     lois = Loi.objects.all()
#     random_lois = random.sample(list(lois), min(len(lois), 10))  # Sélectionne aléatoirement 5 lois
#     return render(request, 'app/home.html', {'actualite': actualites, 'lois': random_lois})


# def home(request):
#     actualites = Actualite.objects.all()
#     lois = Loi.objects.all()
#
#     query = request.GET.get('q')
#     if query:
#         try:
#             lois = Loi.objects.filter(numero_article=int(query))
#             # Passer un paramètre d'ancrage pour diriger vers la section des lois
#             anchor = "#Lois"
#         except ValueError:
#             lois = Loi.objects.none()  # Aucun résultat si la recherche n'est pas un entier
#             anchor=""
#     random_lois = random.sample(list(lois), min(len(lois), 10))  # Sélectionne aléatoirement 10 lois (ou moins si moins de 10 résultats)
#
#     return render(request, 'app/home.html', {'actualites': actualites, 'lois': random_lois})

def partenaire(request):
    partenaires = Partenaire.objects.all()

    return render(request, 'app/base.html', {'partenaires': partenaires})


# def home(request):
#     actualites = Actualite.objects.all()
#     lois = Loi.objects.all()
#
#     if request.method == 'POST':  # Vérifiez si le formulaire a été soumis
#         form = ContactForm(request.POST)  # Créez une instance du formulaire avec les données soumises
#         if form.is_valid():  # Vérifiez si le formulaire est valide
#             form.save()  # Enregistrez les données du formulaire dans la base de données en utilisant la vue contact existante
#             return render(request, 'app/confirmation.html')  # Redirigez vers une page de confirmation ou affichez un message de confirmation
#     else:
#         form = ContactForm()  # Créez une instance vide du formulaire s'il s'agit d'une requête GET
#
#     random_lois = random.sample(list(lois), min(len(lois), 10))  # Sélectionne aléatoirement 10 lois (ou moins si moins de 10 résultats)
#
#     return render(request, 'app/home.html', {'actualites': actualites,'partenaire': partenaire, 'lois': random_lois, 'form': form})
#
from .models import Partenaire  # Importez le modèle Partenaire

def base(request):
    partenaires = Partenaire.objects.all()  # Récupérez tous les partenaires de la base de données

    return render(request, 'app/base.html', {'partenaires': partenaires})

def home(request):
    actualites = Actualite.objects.all()
    lois = Loi.objects.all()

    partenaires = Partenaire.objects.all()  # Récupérez tous les partenaires de la base de données

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'app/confirmation.html')
    else:
        form = ContactForm()

    random_lois = random.sample(list(lois), min(len(lois), 10))

    return render(request, 'app/home.html', {'actualites': actualites, 'partenaires': partenaires, 'lois': random_lois, 'form': form})


def all_lois(request):
    lois = Loi.objects.all()
    return render(request, 'app/all_lois.html', {'lois': lois})

def all_actualites(request):
    actualites = Actualite.objects.all()
    return render(request, 'app/all_actualites.html', {'actualites': actualites})


def video_list(request):
    videos = RessourceVideo.objects.all()
    return render(request, 'app/video_list.html', {'videos': videos})



def actualite_detail(request, pk):
    actualite = get_object_or_404(Actualite, pk=pk)
    return render(request, 'app/actualite_detail.html', {'actualite': actualite})


def all_ressources(request):
    ressources = RessourceEducative.objects.all()
    return render(request, 'app/all_ressources.html', {'ressources': ressources})

def all_pdf_ressources(request):
    ressources_pdf = RessourcePdf.objects.all()
    return render(request, 'app/all_pdf_ressources.html', {'ressources_pdf': ressources_pdf})


def loi_detail(request, loi_id):
    loi = get_object_or_404(Loi, pk=loi_id)
    return render(request, 'app/loi_detail.html', {'loi': loi})


def conseils_securite(request):
    conseils = ConseilSecurite.objects.all().order_by('categorie', 'numero').values()

    conseils_par_categorie = {}
    for categorie, conseils_dans_categorie in groupby(conseils, key=lambda x: x['categorie']):
        conseils_par_categorie[categorie] = list(conseils_dans_categorie)

    return render(request, 'app/conseils_securite.html', {'conseils_par_categorie': conseils_par_categorie})


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



from django.shortcuts import render, get_object_or_404
from .models import Quiz




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








def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'app/confirmation.html')
    else:
        form = ContactForm()
    return render(request, 'app/formulaire_contact.html', {'form': form})


def future_partenaire(request):
    if request.method == 'POST':
        form = FuturePartenaireForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'app/confirmation.html')

            # Redirection ou traitement supplémentaire ici
    else:
        form = FuturePartenaireForm()

    return render(request, 'app/future_partenaire.html', {'form': form})


def signalement(request):
    if request.method == 'POST':
        form = SignalementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'app/confirmation.html')
    else:
        form = SignalementForm()
    return render(request, 'app/signalement.html', {'form': form})
