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
    conseil = models.TextField()

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


class RessourceVideo(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    video_url = models.URLField()  # Lien vers la vidéo
    video_file = models.FileField(upload_to='app/videos/', null=True, blank=True)  # Champ pour le fichier vidéo local
    thumbnail = models.ImageField(upload_to='app/videos/thumbnails/', blank=True, null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre



class ConseilSecurite(models.Model):
  CATEGORIE_CHOICES = (
    ('Sécurisez vos comptes', 'Sécurisez vos comptes'),
    ('Réseaux sociaux', 'Réseaux sociaux'),
    ('Réseaux et confidentialité', 'Réseaux et confidentialité'),
    ('Gestion des mots de passe', 'Gestion des mots de passe'),
  )

  categorie = models.CharField(max_length=50, choices=CATEGORIE_CHOICES)
  numero = models.IntegerField()
  titre = models.CharField(max_length=255)
  contenu = models.TextField()

  def __str__(self):
    return self.titre


class MessageContact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sujet


class Partenaire(models.Model):
    nom = models.CharField(max_length=200)
    image = models.ImageField(upload_to='app/partenaires/', blank=True, null=True)
    lien_site_web = models.URLField(blank=True, null=True)  # Champ pour le lien du site web
    email = models.EmailField()
    numero = models.IntegerField(blank=True, null=True)

class FuturePartenaire(models.Model):
    nom = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='app/future_partenaires/', blank=True, null=True)
    lien_site_web = models.URLField(blank=True, null=True)  # Champ pour le lien du site web
    telephone = models.IntegerField(blank=True, null=True)
    email = models.EmailField()
    adresse = models.CharField(max_length=255)
    type_partenaire = models.CharField(max_length=50,
                                       choices=[('organisation', 'Organisation'), ('entreprise', 'Entreprise'),
                                                ('autre', 'Autre')])
    secteur_activite = models.CharField(max_length=50)
    # date_prise_contact = models.DateField()
    personne_en_charge = models.CharField(max_length=50)
    notes = models.TextField()
    statut = models.CharField(max_length=50, choices=[('prospect', 'Prospect'), ('en_negociation', 'En négociation'),
                                                      ('partenaire', 'Partenaire')], default='en_negociation')
    def __str__(self):
        return self.nom


class SignalementViolation(models.Model):
    TYPE_CHOICES = (
        ('fuite_donnees', 'Fuite de données personnelles'),
        ('acces_non_autorise', 'Accès non autorisé'),
        ('hameconnage', 'Hameçonnage (phishing)'),
        ('autre', 'Autre'),
    )
    GRAVITE_CHOICES = (
        ('faible', 'Faible'),
        ('moyenne', 'Moyenne'),
        ('elevee', 'Élevée'),
    )
    STATUT_CHOICES = (
        ('en_cours', 'En cours d\'investigation'),
        ('resolu', 'Résolu'),
        ('ferme', 'Fermé'),
    )

    type_violation = models.CharField(max_length=50, choices=TYPE_CHOICES, default='autre')
    description = models.TextField()
    preuves = models.FileField(upload_to='app/signalements/', blank=True, null=True)
    date_incident = models.DateTimeField(auto_now_add=True)
    gravite = models.CharField(max_length=10, choices=GRAVITE_CHOICES, default='faible')
    # systeme_affecte = models.CharField(max_length=255, blank=True, null=True)
    # mesures_prises = models.TextField(blank=True, null=True)
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='en_cours')

    def __str__(self):
        return f"Signalement #{self.id} - {self.type_violation}"
