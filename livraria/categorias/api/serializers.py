
from rest_framework import serializers
from livros.models import Livros


class LivroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Livros
        fields = ['nome', 'autorid', 'categoriaid', 'id']
