from serializers import AutorSerializer
from rest_framework.viewsets import ModelViewSet
from autores.models import Autor
    
class LivroViewset(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer