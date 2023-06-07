from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from autores.api.viewset import AutorViewset
from categorias.api.viewset import CategoriaViewset
from livros.api.viewset import LivroViewset


router = routers.DefaultRouter()
router.register(r"livros", LivroViewset)
router.register(r"categorias", CategoriaViewset)
router.register(r"Autores", AutorViewset)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
]