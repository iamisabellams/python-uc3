from django.db import models
from django.contrib.auth.models import User

class TagNoticia(models.Model):
    descricao = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.descricao

class CategoriaNoticia(models.Model):
    descricao = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.descricao

class Noticia(models.Model):
    STATUS_CHOICES = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )
    titulo = models.CharField(max_length=255)
    resumo = models.TextField()
    conteudo = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='rascunho')
    data_publicacao = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(TagNoticia, related_name='noticias')
    categoria = models.ForeignKey(CategoriaNoticia, on_delete=models.SET_NULL, null=True, related_name='noticias')

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('rejeitado', 'Rejeitado'),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comentarios'
    )
    noticia = models.ForeignKey(
        Noticia, 
        on_delete=models.CASCADE,
        related_name='comentarios'
    )
    conteudo = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário de {self.user.username} em {self.noticia.titulo}'