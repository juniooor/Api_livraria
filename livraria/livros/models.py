from django.db import models
from autores.models import Autor
from categorias.models import Categoria


class Livros(models.Model):
    nome = models.CharField(max_length=120)
    autores = models.ManyToManyField(Autor)
    categorias = models.ManyToManyField(Categoria)
    
    def __str__(self):
        return self.nome
