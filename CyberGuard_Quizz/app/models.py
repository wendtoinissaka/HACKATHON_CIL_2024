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
    lien_site_web = models.URLField(blank=True, null=True)  # Champ pour le lien du site web

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

    def __str__(self):
        return f"Loi {self.numero_article}"


class MessageUtilisateur(models.Model):
    nom = models.CharField(max_length=100)
    adresse_email = models.EmailField()
    objet = models.CharField(max_length=50)
    message = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)





class RessourceEducative(models.Model):
    TIPES_RESSOURCE = (
        ('article', 'Article'),
        ('video', 'Vidéo'),
        ('document', 'Document'),
    )
    image = models.ImageField(upload_to='app/images/ressources_images', default='app/images/default_quiz_image.png', null=True, blank=True)
    titre = models.CharField(max_length=100)
    description = models.TextField()
    type_ressource = models.CharField(max_length=50, choices=TIPES_RESSOURCE)

    def __str__(self):
        return self.titre


class RessourcePdf(models.Model):
    # image = models.ImageField(upload_to='app/images/ressources_images', default='app/images/default_quiz_image.png', null=True, blank=True)
    titre = models.CharField(max_length=100)
    description = models.TextField()
    fichier = models.FileField(upload_to='app/pdfs')
    def __str__(self):
        return self.titre



# class SecurityAdvice(models.Model):
#   """Model for storing and managing security advice."""
#
#   name = models.CharField(max_length=255, unique=True)  # Unique identifier for advice
#   description = models.TextField()  # Brief description of the advice
#   created_date = models.DateTimeField(auto_now_add=True)  # Date of creation
#   updated_date = models.DateTimeField(auto_now=True)  # Date of last update
#   author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)  # Author (optional)
#   source = models.URLField(blank=True)  # Link to original source (optional)
#
#   # Content related fields
#   title = models.CharField(max_length=255)  # Title of the advice
#   content = models.TextField()  # Detailed content of the advice
#   risk_level = models.CharField(max_length=50, choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')])  # Risk level
#   target_audience = models.CharField(max_length=255, blank=True)  # Intended users (optional)
#   keywords = models.CharField(max_length=255, blank=True)  # Keywords for search
#
#   # Metadata fields
#   category = models.ForeignKey('SecurityCategory', on_delete=models.CASCADE)  # Category of advice (e.g., data protection)
#   format = models.CharField(max_length=50, choices=[('ARTICLE', 'Article'), ('GUIDE', 'Guide'), ('TUTORIAL', 'Tutorial'), ('VIDEO', 'Video')])  # Format of the advice
#   duration = models.CharField(max_length=50, blank=True)  # Approximate time to follow the advice (optional)
#   language = models.CharField(max_length=10, blank=True)  # Language of the advice (optional)
#
#   # Additional resources
#   resources = models.ManyToManyField('Resource', blank=True)  # Links to related resources
#
#   # Consider adding interactive features (forms, comments) using separate models linked to this one
#
#   class Meta:
#     ordering = ['-created_date']  # Order by creation date (newest first)
#
#   def __str__(self):
#     return self.title
