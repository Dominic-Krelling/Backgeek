from django.db import models
from uploader.models import Image

class Camiseta(models.Model):
    titulo = models.CharField(max_length=999)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, null=True, blank=True
    )
    imagem = models.ManyToManyField(
        Image, related_name="Camiseta")
        
    def __str__(self):
        return f"{self.titulo} ({self.preco})"
    class Meta:
        verbose_name = "Camiseta"
        verbose_name_plural = "Camisetas"

    def first_image(self):
        return self.imagem.all()[0].url

class Estampa(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descricao} ({self.id})"

class Moletom(models.Model):
    titulo = models.CharField(max_length=999)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, null=True, blank=True
    )
    imagem = models.ManyToManyField(
        Image, related_name="Moletom")
        
    def __str__(self):
        return f"{self.titulo} ({self.preco})"
    class Meta:
        verbose_name = "Moletom"
        verbose_name_plural = "Moletons"

    def first_image(self):
        return self.imagem.all()[0].url
    

class Categoria(models.Model):
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titulo}"

class Produto(models.Model):
    titulo = models.CharField(max_length=999)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros"
    )
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    def __str__(self):
        return f"{self.titulo} ({self.preco})"
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"