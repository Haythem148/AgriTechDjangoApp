# Generated by Django 5.1.2 on 2024-10-29 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionEngrais', '0002_alter_applicationengrais_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationengrais',
            name='analyse_sol',
            field=models.JSONField(default=dict, help_text="Données d'analyse du sol"),
        ),
        migrations.AddField(
            model_name='applicationengrais',
            name='conditions_meteo',
            field=models.JSONField(default=dict, help_text='Conditions météorologiques'),
        ),
        migrations.AlterField(
            model_name='applicationengrais',
            name='ia',
            field=models.JSONField(default=dict, help_text="Stockage des recommandations d'IA", verbose_name='AI Optimization'),
        ),
    ]