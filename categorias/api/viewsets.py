from rest_framework import viewsets, permissions
from categorias.api import serializers
from django.contrib.auth.models import User
from categorias import models

class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategoriaSerializer
    queryset = models.Categoria.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #apenas permite ver

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]
