from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from django.utils import timezone
from django.core import validators


class Curso(models.Model):
    STATUSLISTA = (
        ('basico', 'Básico'),
        ('intermediario', 'Intermediário'),
        ('avancado', 'Avançado'),
    )

    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    descricao_curta = models.CharField(max_length=180)
    horas = models.CharField(max_length=100)
    tipo = models.CharField(
        max_length=13,
        choices=STATUSLISTA,
        default='basico',
    )
    imagem = models.ImageField(upload_to='media/curso/capa', null=True, blank=True)
    selo = models.ImageField(upload_to='media/curso/selo', null=True, blank=True)
    selo_cinza = models.ImageField(upload_to='media/curso/selo', null=True, blank=True)
    selo_prova = models.ImageField(upload_to='media/curso/selo', null=True, blank=True)
    selo_prova_cinza = models.ImageField(upload_to='media/curso/selo', null=True, blank=True)
    selo_max = models.ImageField(upload_to='media/curso/selo', null=True, blank=True)
    selo_cinza_max = models.ImageField(upload_to='media/curso/selo', null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    video_curso = models.CharField(max_length=800)
    def __str__(self):
        return self.nome


class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, validators=[validators.EmailValidator()])
    nome_completo = models.CharField(max_length=255)
    genero = models.CharField(
        max_length=2,
        default='',
        choices=(
            ('H', 'Homem'),
            ('M', 'Mulher'),
            ('O', 'Outros'),
        )
    )
    endereco = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(
        max_length=2,
        default='RS',
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )  
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    data_nascimento = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=255, blank=True, null=True)
    foto = models.ImageField(upload_to='media/aluno/foto')
    cadastro_completo = models.BooleanField(default=False)
    tour_completo = models.BooleanField(default=True)
    tour_dig_completo = models.BooleanField(default=True)

    def __str__(self):
         return self.user.username



class Licao(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    video = models.TextField()
    botao = models.FileField(upload_to='media/curso/downloads', blank=True, null=True)
    ordem = models.IntegerField()
    categoria = models.CharField(max_length=200)
    categoria_ordem = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    demo = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Inscricao(models.Model):
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_inscricao = models.DateTimeField(auto_now_add=True)
    categoria_licao = models.IntegerField(default='1')

    def __str__(self):
         return self.aluno.username + ' <-> ' + self.curso.nome


class ConclusaoLicao(models.Model):

    STATUSLISTA = (
        ('fazer', 'Fazer'),
        ('concluido', 'Concluido'),
    )

    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    licao = models.ForeignKey(Licao, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=9,
        choices=STATUSLISTA,
        default='fazer',
    )
    data_conclusao = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.aluno.username}'
    
class DigitacaoDetalhes(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    descricao_curta = models.CharField(max_length=255)
    valor = models.IntegerField()
    horas = models.IntegerField()
    licoes = models.IntegerField()
    
    def __str__(self):
        return str(self.nome)
    
class Digitacao(models.Model):
    STATUSLISTA = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    )
    ordem = models.IntegerField()
    descricao = models.TextField()
    repeticao = models.IntegerField()
    licao = models.CharField(max_length=255)
    fase = models.CharField(
        max_length=6,
        choices=STATUSLISTA,
        default='1',
    )

    def __str__(self):
        return f'{self.licao}'

class InscricaoDigitacao(models.Model):
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    digitacao = models.ForeignKey(Digitacao, on_delete=models.CASCADE)
    licao_atual = models.IntegerField(default='1')
    contador_licao = models.IntegerField(default='0')
    data_inscricao = models.DateTimeField(default=timezone.now)
    data_acesso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.aluno.username
    
class RelatorioDigitacao(models.Model):
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    licao_atual = models.IntegerField()
    data_acesso = models.DateTimeField(auto_now_add=True)
    toques = models.IntegerField()
    acertos = models.DecimalField(max_digits=6, decimal_places=2)
    erros = models.IntegerField()
    tempo = models.CharField(max_length=255)
    
    def __str__(self):
         return self.aluno.username


class ProvaDigitacao(models.Model):
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    data_conclusao = models.DateTimeField(auto_now_add=True)
    toques = models.IntegerField(null=True, blank=True)
    nota = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    tempo = models.CharField(max_length=255, null=True, blank=True)
    erros = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
         return self.aluno.username


class Questao(models.Model):
    TIPO_CHOICES = (
        ('checks', 'Checks'),
        ('radios', 'Radios'),
    )

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    enunciado = models.TextField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    def __str__(self):
        return self.enunciado

class ItemQuestao(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    correto = models.BooleanField()

    def __str__(self):
        return self.texto


class Resposta(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    data_resposta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno} - {self.curso}"
    
    