
from rest_framework import serializers
from autores.models import Autor


class AutorSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = ['nome','id']
