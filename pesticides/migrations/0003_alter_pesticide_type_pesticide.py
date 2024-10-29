# Generated by Django 5.1.2 on 2024-10-29 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pesticides', '0002_remove_application_parcelle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesticide',
            name='type_pesticide',
            field=models.CharField(choices=[('herbicide', 'Herbicide'), ('insecticide', 'Insecticide'), ('fongicide', 'Fongicide'), ('autre', 'Autre')], max_length=20, verbose_name='Type de pesticide'),
        ),
    ]
