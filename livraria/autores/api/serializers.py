
from rest_framework import serializers
from autores.models import Autor


class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = ['nome','id']
