# Generated by Django 5.1.2 on 2024-10-29 20:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Engrais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('composition', models.CharField(max_length=255)),
                ('recommandation_dose', models.FloatField()),
                ('type_sol', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationEngrais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('quantite', models.FloatField()),
                ('ia', models.TextField()),
                ('engrais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionEngrais.engrais')),
            ],
        ),
    ]
