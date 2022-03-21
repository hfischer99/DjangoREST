from rest_framework import serializers
from imoveis import models

class CasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Casa
        fields = '__all__'

class OrcamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Orcamento
        fields = '__all__'