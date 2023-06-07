from django.db import models
from autores.models import Autor
from categorias.models import Categoria

class Livros(models.Model):
    nome = models.CharField(max_length=120)
    autorid = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoriaid = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
