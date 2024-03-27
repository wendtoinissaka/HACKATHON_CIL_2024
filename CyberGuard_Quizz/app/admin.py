from django.contrib import admin
from .models import ConseilDeSecurite, Actualite, Quiz, Question

class ConseilDeSecuriteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'contenu', 'date_publication')
    search_fields = ('titre', 'contenu')
    list_filter = ('date_publication',)

class ActualiteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'contenu', 'date_publication')
    search_fields = ('titre', 'contenu')
    list_filter = ('date_publication',)

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class QuizAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description', 'difficulte')
    search_fields = ('titre', 'description')
    list_filter = ('difficulte',)
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('enonce', 'quiz', 'reponse_correcte')
    search_fields = ('enonce',)
    list_filter = ('quiz',)

admin.site.register(ConseilDeSecurite, ConseilDeSecuriteAdmin)
admin.site.register(Actualite, ActualiteAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
