from django.db import models

class Tag(models.Model):
    descricao = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.descricao

class CategoriaProduto(models.Model):
    descricao = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.descricao

class Marca(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produto_imagens/', blank=True, null=True)
    qt_estoque = models.IntegerField(default=0)
    tamanho = models.CharField(max_length=50, blank=True, null=True)

  
    tags = models.ManyToManyField(Tag, related_name='produtos') 
    categoria = models.ForeignKey(CategoriaProduto, on_delete=models.SET_NULL, null=True, related_name='produtos')
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, related_name='produtos')

    def __str__(self):
        return self.nome