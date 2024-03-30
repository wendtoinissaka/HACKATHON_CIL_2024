from django import forms
from .models import MessageContact, FuturePartenaire
from django_recaptcha.fields import ReCaptchaField


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = MessageContact
        fields = ['nom', 'email', 'sujet', 'message', 'captcha']




class FuturePartenaireForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = FuturePartenaire
        exclude = ['statut']
        widgets = {
            'date_prise_contact': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(FuturePartenaireForm, self).__init__(*args, **kwargs)


# class FuturePartenaireForm(forms.ModelForm):
#     class Meta:
#         model = FuturePartenaire
#         exclude = ['statut']  # Exclure les champs 'notes' et 'statut'
#
#     def __init__(self, *args, **kwargs):
#         super(FuturePartenaireForm, self).__init__(*args, **kwargs)

