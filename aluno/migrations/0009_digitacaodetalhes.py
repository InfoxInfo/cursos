# Generated by Django 4.2 on 2024-08-23 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0008_aluno_bairro_aluno_cep_aluno_cidade_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DigitacaoDetalhes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField()),
                ('horas', models.IntegerField()),
                ('licoes', models.IntegerField()),
            ],
        ),
    ]