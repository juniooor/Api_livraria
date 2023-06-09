
from rest_framework import serializers
from livros.models import Livros
from autores.models import Autor
from categorias.models import Categoria

        
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields =  ['nome','id']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nome','id']


class LivroSerializers(serializers.ModelSerializer):
    autor = AutorSerializer()
    categoria = CategoriaSerializer(many=True)

    class Meta:
        model = Livros
        fields = ['id', 'nome', 'autor', 'categoria']