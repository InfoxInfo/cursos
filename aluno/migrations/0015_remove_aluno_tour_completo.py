# Generated by Django 4.2 on 2024-09-27 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0014_aluno_tour_completo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='tour_completo',
        ),
    ]