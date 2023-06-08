from .serializers import CategoriaSerializers
from rest_framework.viewsets import ModelViewSet
from categorias.models import Categoria
    
class CategoriaViewset(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers