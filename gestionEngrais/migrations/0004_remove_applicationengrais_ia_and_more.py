# Generated by Django 5.1.2 on 2024-10-29 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionEngrais', '0003_applicationengrais_analyse_sol_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationengrais',
            name='ia',
        ),
        migrations.AddField(
            model_name='applicationengrais',
            name='historique_applications',
            field=models.JSONField(default=dict, help_text='Historique des applications précédentes'),
        ),
        migrations.AddField(
            model_name='applicationengrais',
            name='recommandations_ia',
            field=models.JSONField(default=dict, help_text="Recommandations générées par l'IA"),
        ),
    ]