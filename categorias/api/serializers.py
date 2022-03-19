from rest_framework import serializers
from django.contrib.auth.models import User
from categorias import models

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categoria
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']