# Generated by Django 4.2.11 on 2024-03-28 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_ressourceeducative'),
    ]

    operations = [
        migrations.CreateModel(
            name='RessourcePdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('lien', models.CharField(max_length=50)),
            ],
        ),
    ]