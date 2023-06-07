from serializers import LivroSerializer
from rest_framework.viewsets import ModelViewSet
from livros.models import Livros
    
class LivroViewset(ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivroSerializer