# Generated by Django 4.2.11 on 2024-03-28 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_chapitre_loi_titre_loi_actualite_image_loi'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapitre_loi',
            name='titre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='chapitre_loi', to='app.titre_loi'),
            preserve_default=False,
        ),
    ]
