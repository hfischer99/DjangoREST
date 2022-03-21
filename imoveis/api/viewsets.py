from rest_framework import viewsets, permissions
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from imoveis.api import serializers
from imoveis import models

class CasaViewSet(viewsets.ModelViewSet):
    queryset = models.Casa.objects.all()
    serializer_class = serializers.CasaSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrcamentoViewSet(viewsets.ModelViewSet):
    queryset = models.Orcamento.objects.all()
    serializer_class = serializers.OrcamentoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, **kwargs):
        valor = request.POST['valor']
        instance = models.Orcamento.objects.create(valor=valor)
        #chama o post_save, para retornar as casas encontradas
        instance.post_save()
        serializer = serializers.OrcamentoSerializer(instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        valor = request.POST['valor']
        instance = models.Orcamento.objects.get(id=pk)
        instance.valor = valor
        instance.save()
        instance.post_save()
        serializer = serializers.OrcamentoSerializer(instance)
        return Response(serializer.data)


    def destroy(self, request, pk=None):
        raise MethodNotAllowed(method='DELETE')