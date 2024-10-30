# Generated by Django 4.2.5 on 2024-10-29 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0001_initial'),
        ('water_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilisationeau',
            name='parcelle',
        ),
        migrations.AddField(
            model_name='utilisationeau',
            name='farm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='utilisations', to='farms.farm'),
        ),
    ]
