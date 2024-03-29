from django.contrib import admin
from .models import ConseilDeSecurite, Actualite, Quiz, Question, Loi, Titre_loi, Chapitre_loi, RessourceEducative, \
    RessourcePdf


@admin.register(ConseilDeSecurite)
class ConseilDeSecuriteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'contenu', 'date_publication')
    search_fields = ('titre', 'contenu')
    list_filter = ('date_publication',)

@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'contenu', 'date_publication')
    search_fields = ('titre', 'contenu')
    list_filter = ('date_publication',)

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description', 'difficulte')
    search_fields = ('titre', 'description')
    list_filter = ('difficulte',)
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('enonce', 'quiz', 'reponse_correcte')
    search_fields = ('enonce',)
    list_filter = ('quiz',)

@admin.register(Loi)
class LoiAdmin(admin.ModelAdmin):
    list_display = ('numero_article', 'titre', 'chapitre',)
    search_fields = ('titre','chapitre')
    list_filter = ('titre',)


@admin.register(Titre_loi)
class Titre_loiAdmin(admin.ModelAdmin):
    list_display = ('numero_titre','nom_titre',)


@admin.register(Chapitre_loi)
class Chapitre_loiAdmin(admin.ModelAdmin):
    list_display = ('numero_chapitre','nom_chapitre',)

@admin.register(RessourceEducative)
class RessourceEducativeAdmin(admin.ModelAdmin):
    list_display = ('type_ressource','titre',)


@admin.register(RessourcePdf)
class RessourcePdfAdmin(admin.ModelAdmin):
    list_display = ('titre','description',)


# admin.site.register(ConseilDeSecurite, ConseilDeSecuriteAdmin)
# admin.site.register(Actualite, ActualiteAdmin)
# admin.site.register(Quiz, QuizAdmin)
# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Loi, LoiAdmin)
