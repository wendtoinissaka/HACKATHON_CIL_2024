# Generated by Django 4.2.11 on 2024-03-29 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_ressourcepdf_lien_ressourcepdf_fichier'),
    ]

    operations = [
        migrations.AddField(
            model_name='actualite',
            name='lien_site_web',
            field=models.URLField(blank=True, null=True),
        ),
    ]