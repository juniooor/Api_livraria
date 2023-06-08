
from rest_framework import serializers
from categorias.models import Categoria


class CategoriaSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nome',  'id']
