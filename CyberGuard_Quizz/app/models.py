from django.db import models
import random

class ConseilDeSecurite(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

class Actualite(models.Model):
    image = models.ImageField(upload_to='app/images/actualite_images', default='app/images/default_actualite_image.png', null=True, blank=True)
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre



class Quiz(models.Model):
    DIFFICULTE = (
        ('Facile', 'Facile'),
        ('Intermediaire', 'Intermédiaire'),
        ('Difficile', 'Difficile'),
    )
    titre = models.CharField(max_length=100)
    description = models.TextField()
    difficulte = models.CharField(max_length=50, choices=DIFFICULTE)
    # image = models.ImageField(upload_to='quiz_images/', null=True, blank=True)
    image = models.ImageField(upload_to='app/images/quiz_images', default='app/images/default_quiz_image.png', null=True, blank=True)
    date_modification = models.DateTimeField(auto_now=True)  # Champ de date de modification automatiquement mis à jour à chaque modification
    def __str__(self):
        return self.titre

    class Meta:
        ordering = ['-date_modification']  # Ordonner les quiz par date de modification décroissante par défaut


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    enonce = models.TextField()
    choix_1 = models.CharField(max_length=200)
    choix_2 = models.CharField(max_length=200)
    choix_3 = models.CharField(max_length=200)
    choix_4 = models.CharField(max_length=200)
    reponse_correcte = models.IntegerField(choices=((1, 'Choix 1'), (2, 'Choix 2'), (3, 'Choix 3'), (4, 'Choix 4')))

    def get_random_questions(self, count):
        questions = list(self.questions.all())
        random.shuffle(questions)
        return questions[:count]


def __str__(self):
        return self.texte_question


class Titre_loi(models.Model):
    numero_titre = models.IntegerField()
    nom_titre = models.CharField(max_length=100)
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_titre


class Chapitre_loi(models.Model):
    numero_chapitre = models.IntegerField()
    nom_chapitre = models.CharField(max_length=100)
    date_publication = models.DateTimeField(auto_now_add=True)
    titre = models.ForeignKey(Titre_loi, on_delete=models.CASCADE, related_name='chapitre_loi')

    def __str__(self):
        return self.nom_chapitre


class Loi(models.Model):
    numero_article = models.IntegerField(unique=True)
    titre = models.ForeignKey(Titre_loi, on_delete=models.CASCADE, related_name='loi')
    chapitre = models.ForeignKey(Chapitre_loi, on_delete=models.CASCADE, related_name='loi')
    description = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)


class MessageUtilisateur(models.Model):
    nom = models.CharField(max_length=100)
    adresse_email = models.EmailField()
    objet = models.CharField(max_length=50)
    message = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)




# from django.db import models
# from django.contrib.auth.models import User
#
# class Quiz(models.Model):
#     DIFFICULTE_CHOICES = [
#         ('Facile', 'Facile'),
#         ('Moyen', 'Moyen'),
#         ('Difficile', 'Difficile'),
#     ]
#     titre = models.CharField(max_length=100)
#     description = models.TextField()
#     difficulte = models.CharField(max_length=50, choices=DIFFICULTE_CHOICES)
#
#     def __str__(self):
#         return self.titre
#
# class Question(models.Model):
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#     texte_question = models.TextField()
#     option1 = models.CharField(max_length=200)
#     option2 = models.CharField(max_length=200)
#     option3 = models.CharField(max_length=200)
#     option4 = models.CharField(max_length=200)
#     reponse_correcte = models.CharField(max_length=1, choices=(('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C'), ('D', 'Option D')))
#
#     def __str__(self):
#         return self.texte_question
#
# class ConseilSecurite(models.Model):
#     texte_conseil = models.TextField()
#     reponse_declenchante = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.texte_conseil
#
# class RessourceEducative(models.Model):
#     TYPE_CHOICES = [
#         ('article', 'Article'),
#         ('video', 'Vidéo'),
#         ('infographie', 'Infographie'),
#     ]
#     titre = models.CharField(max_length=100)
#     description = models.TextField()
#     type_ressource = models.CharField(max_length=50, choices=TYPE_CHOICES)
#
#     def __str__(self):
#         return self.titre
#
# class ProfilUtilisateur(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Ajoutez d'autres champs de profil utilisateur au besoin
#
#     def __str__(self):
#         return self.user.username
#
# class ProgressionQuiz(models.Model):
#     utilisateur = models.ForeignKey(ProfilUtilisateur, on_delete=models.CASCADE)
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#     score = models.FloatField()
#
#     def __str__(self):
#         return f"{self.utilisateur.user.username} - {self.quiz.titre} - {self.score}"
#
# class StatistiquesUtilisation(models.Model):
#     date = models.DateField(auto_now_add=True)
#     nombre_utilisateurs = models.IntegerField()
#     # Ajoutez d'autres champs de statistiques au besoin
#
#     def __str__(self):
#         return str(self.date)
#
#
# # from django.db import models
#
# # # Create your models here.
# # from django.db import models
# # from django.contrib.auth.models import User
#
# # class Quiz(models.Model):
# #     DIFFICULTE = (
# #         ('Facile', 'Facile'),
# #         ('Intermediaire', 'Intermédiaire'),
# #         ('Difficile', 'Difficile'),
# #     )
# #     titre = models.CharField(max_length=100)
# #     description = models.TextField()
# #     difficulte = models.CharField(max_length=50, choices=DIFFICULTE)
#
# #     def __str__(self):
# #         return self.titre
#
# # class Question(models.Model):
# #     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
# #     texte_question = models.TextField()
# #     option1 = models.CharField(max_length=200)
# #     option2 = models.CharField(max_length=200)
# #     option3 = models.CharField(max_length=200)
# #     option4 = models.CharField(max_length=200)
# #     reponse_correcte = models.CharField(max_length=200)
#
# #     def __str__(self):
# #         return self.texte_question
#
# # class ConseilSecurite(models.Model):
# #     texte_conseil = models.TextField()
# #     reponse_declenchante = models.CharField(max_length=200)
#
# #     def __str__(self):
# #         return self.texte_conseil
#
# # class RessourceEducative(models.Model):
# #     TIPES_RESSOURCE = (
# #         ('article', 'Article'),
# #         ('video', 'Vidéo'),
# #         ('infographie', 'Infographie'),
# #     )
# #     titre = models.CharField(max_length=100)
# #     description = models.TextField()
# #     type_ressource = models.CharField(max_length=50, choices=TIPES_RESSOURCE)
#
# #     def __str__(self):
# #         return self.titre
#
# # class ProfilUtilisateur(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     progression_quiz = models.ManyToManyField(Quiz, through='ProgressionQuiz')
# #     conseils_personnalises = models.ManyToManyField(ConseilSecurite)
# #     # Ajoutez d'autres champs de profil utilisateur au besoin
#
# #     def __str__(self):
# #         return self.user.username
#
# # class ProgressionQuiz(models.Model):
# #     utilisateur = models.ForeignKey(ProfilUtilisateur, on_delete=models.CASCADE)
# #     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
# #     score = models.FloatField()
#
# #     def __str__(self):
# #         return f"{self.utilisateur.user.username} - {self.quiz.titre} - {self.score}"
#
# # class StatistiquesUtilisation(models.Model):
# #     date = models.DateField(auto_now_add=True)
# #     nombre_utilisateurs = models.IntegerField()
# #     # Ajoutez d'autres champs de statistiques au besoin
#
# #     def __str__(self):
# #         return str(self.date)
