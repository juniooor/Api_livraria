
from rest_framework import serializers
from livros.models import Livros


class LivroSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Livros
        fields = ['nome', 'autorid', 'categoriaid', 'id']
