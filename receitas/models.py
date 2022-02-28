from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Classe Categoria a ser implementada
'''class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_categoria'''


class Receita(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    date_receita = models.DateTimeField(default=datetime.now, blank=True)
    publicar = models.BooleanField(default=False)
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
    #categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.nome_receita
