# Generated by Django 4.2 on 2024-09-27 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0013_alter_licao_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='tour_completo',
            field=models.BooleanField(default=False),
        ),
    ]
