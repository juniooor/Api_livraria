from .serializers import AutorSerializers
from rest_framework.viewsets import ModelViewSet
from autores.models import Autor
    
class AutorViewset(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializers