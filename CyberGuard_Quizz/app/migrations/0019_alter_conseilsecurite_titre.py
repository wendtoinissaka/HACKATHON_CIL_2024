# Generated by Django 4.2.11 on 2024-03-29 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_conseilsecurite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conseilsecurite',
            name='titre',
            field=models.CharField(choices=[('Sécurisez vos comptes', 'Sécurisez vos comptes'), ('Les réseaux sociaux', 'Les réseaux sociaux'), ('Réseaux et confidentialité', 'Réseaux et confidentialité'), ('Gestion des mots de passe', 'Gestion des mots de passe')], max_length=100),
        ),
    ]
