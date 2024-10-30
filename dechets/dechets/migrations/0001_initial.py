# Generated by Django 5.1.2 on 2024-10-29 17:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeDechet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom du type de déchet')),
                ('biodegradable', models.BooleanField(default=False, verbose_name='Biodégradable')),
                ('methode_traitement', models.CharField(max_length=200, verbose_name='Méthode de traitement')),
            ],
            options={
                'verbose_name': 'Type de déchet',
                'verbose_name_plural': 'Types de déchets',
            },
        ),
        migrations.CreateModel(
            name='PlanGestionDechets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.FloatField(verbose_name='Quantité (kg)')),
                ('date', models.DateField(verbose_name='Date de génération')),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.farm', verbose_name='Exploitation agricole')),
                ('type_dechet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dechets.typedechet', verbose_name='Type de déchet')),
            ],
            options={
                'verbose_name': 'Plan de gestion des déchets',
                'verbose_name_plural': 'Plans de gestion des déchets',
            },
        ),
    ]
