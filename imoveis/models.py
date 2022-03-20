from django.db import models
from datetime import datetime
from decimal import Decimal
from django.conf import settings
from django.urls import reverse
from django.db.models import Sum

class Casa(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    valor = models.DecimalField(verbose_name='Valor', max_digits=10, decimal_places=2)

class Orcamento(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    valor = models.DecimalField(verbose_name='Valor para Investimento', max_digits=10, decimal_places=2)
    data = models.DateTimeField(verbose_name='Data', default=datetime.now, editable=False)
    casas = models.ManyToManyField(Casa, editable=False, verbose_name='Casas')
    valor_remanescente = models.DecimalField(verbose_name='Valor Remanescente', max_digits=10, decimal_places=2, editable=False, null=True, blank=True)
    investimento_total = models.DecimalField(verbose_name='Total do Investimento', max_digits=10, decimal_places=2, editable=False, null=True, blank=True)

    def post_save(self, request=None):
        self.quantidade_casas(self.valor)
        self.data = datetime.now()
        self.save()

    def quantidade_casas(self, valor):
        if valor == None:
            return
        try:
            valor = Decimal(valor)
        except:
            return
        if valor <= Decimal(0):
            return

        valor_compra = valor
        total_investido = Decimal(0)
        for casa in Casa.objects.filter(valor__lte=self.valor).order_by('valor'):
            if settings.DEBUG:
                print('Casa:', casa.id, 'Valor:', casa.valor, 'Orcamento Restante:', valor_compra)
            if valor_compra >= casa.valor:
                self.casas.add(casa)
                valor_compra = valor_compra - casa.valor
                total_investido = total_investido + casa.valor
                continue
            if valor_compra <= Decimal(0):
                break

        self.valor_remanescente = valor_compra
        self.investimento_total = total_investido
        self.save()