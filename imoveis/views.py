from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def orcamento_view(request,  pk=None):
    from .models import Orcamento
    orcamento = Orcamento.objects.get(id=pk)
    context = {
        'orcamento': orcamento
    }
    return render(request, 'orcamento.html', context)
