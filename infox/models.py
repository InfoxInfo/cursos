from django.db import models


class InfoxModel(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    imagem = models.FileField(upload_to='media/infox/site', blank=True, null=True)
    missao = models.TextField()
    visao = models.TextField()
    valores = models.TextField()
    tituloVideo = models.CharField(max_length=255)
    descricaoVideo = models.TextField()
    videoLink = models.TextField()
    equipeImagem = models.FileField(upload_to='media/infox/site', blank=True, null=True)
    linkMapa = models.TextField()

    def __str__(self):
        return self.titulo



class CursoS(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class CursoSuper(models.Model):
    curso = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.curso

class CursoTecnico(models.Model):
    curso = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.curso

class PosGraduacao(models.Model):
    curso = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.curso

class MBA(models.Model):
    curso = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.curso

class CursoSuperior(models.Model):
    tituloS = models.CharField(max_length=255)
    descricaoTituloS = models.TextField()
    logo = models.ImageField(upload_to='media/infox/logos/', blank=True, null=True)
    imagemCapa = models.ImageField(upload_to='media/infox/', blank=True, null=True)
    descricaoTutora = models.TextField()
    imagemTutora = models.ImageField(upload_to='media/infox/', blank=True, null=True)
    
    def __str__(self):
        return self.tituloS

class LogoEmpresas(models.Model):
    empresa = models.CharField(max_length=255)
    logo_empresa = models.ImageField(upload_to='media/infox/logos_empresas/', blank=True, null=True)

    def __str__(self):
        return self.empresa

class CursoProf(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    imagemLogo = models.FileField(upload_to='media/infox/site/', blank=True, null=True)
    imagemCapa = models.FileField(upload_to='media/infox/site/', blank=True, null=True)

    def __str__(self):
        return self.titulo
    
class LogoEmpresasProf(models.Model):
    empresa = models.CharField(max_length=255)
    logo_empresa = models.ImageField(upload_to='media/infox/logos_empresas_prof/', blank=True, null=True)

    def __str__(self):
        return self.empresa
    
class Pacote(models.Model):
    nome = models.CharField(max_length=120, verbose_name="Nome do Pacote")
    descricao = models.TextField(verbose_name="Descrição do Pacote")
    cor_fundo = models.CharField(max_length=200, verbose_name="Cor de Fundo Padote")
    cor_fundo_tex = models.CharField(max_length=200, verbose_name="Cor de Texto Pacote")
    cor_curso = models.CharField(max_length=200, verbose_name="Cor do Fundo Curso")
    cor_curso_tex = models.CharField(max_length=200, verbose_name="Cor do Texto Curso")

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do Curso")
    pacote = models.ForeignKey(Pacote, on_delete=models.CASCADE, related_name="cursos")

    def __str__(self):
        return self.nome
    
class Turma(models.Model):
    cursoturma = models.CharField(max_length=255)
    descricao_turma = models.TextField(verbose_name="Descrição do curso em turma")
    foto_turma = models.ImageField(upload_to='media/infox/', blank=True, null=True)

    def __str__(self):
        return self.cursoturma
    
class Equipefoto(models.Model):
    equipe = models.CharField(max_length=255)
    foto_equipe = models.ImageField(upload_to='media/infox/equipe', blank=True, null=True)

    def __str__(self):
        return self.equipe

class ContactMe(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=2000)