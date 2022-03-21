"""DjangoREST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from categorias.api import viewsets as categoriaviewsets
from imoveis.api import viewsets as imoveisviewsets
from imoveis.views import orcamento_view

route = routers.DefaultRouter()

route.register(r'categorias', categoriaviewsets.CategoriaViewSet, basename="categorias")
route.register(r'users', categoriaviewsets.UserViewSet)
route.register(r'casas', imoveisviewsets.CasaViewSet, basename="casas")
route.register(r'orcamentos', imoveisviewsets.OrcamentoViewSet, basename="orcamentos")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(route.urls)),
    path(r'orcamento/<int:pk>', orcamento_view, name='imoveis')
]
