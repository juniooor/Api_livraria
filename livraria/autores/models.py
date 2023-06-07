from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=120)
    
    def __str__(self):
        return self.nome