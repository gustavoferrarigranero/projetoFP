# This Python file uses the following encoding: utf-8
# ANOTAÇÃO PARA USAR CARACTERES ESPECIAIS AQUI. (MESMO PARA ANOTAÇÕES.)
""" 
@gustavoferrarigranero
https://www.facebook.com/groups/pythonmania/
"""

from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q #Queries complexas
from caixas.models import Caixa
from pessoas.models import Pessoa
from django.utils import formats
from datetime import datetime

def index(request):
    return render(request, 'index.html')

def caixaListar(request):

    caixas = Caixa.objects.all()[0:10]

    return render(request, 'caixas/listaCaixas.html', {'caixas': caixas})


def caixaAdicionar(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'caixas/formCaixas.html',{'pessoas':pessoas})

def caixaSalvar(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo', '0')

        try:
            caixa = Caixa.objects.get(pk=codigo)
        except:
            caixa = Caixa()

        caixa.pessoa = Pessoa.objects.get(pk=request.POST.get('pessoa', ''))
        caixa.descricao = request.POST.get('descricao', '').upper()
        caixa.tipo = request.POST.get('tipo').upper()
        caixa.valor = request.POST.get('valor', '')
        date_only = datetime.strptime(request.POST.get('data',''), '%d/%m/%Y %H:%M:%S').date()
        caixa.data = date_only

        caixa.save()
        
    return HttpResponseRedirect('/caixas/')

def caixaPesquisar(request):
    self

def caixaEditar(request, pk=0):
    try:
        caixa = Caixa.objects.get(pk=pk)
        pessoas = Pessoa.objects.all()
    except:
        return HttpResponseRedirect('/caixas/')

    return render(request, 'caixas/formCaixas.html', {'caixa': caixa,'pessoas':pessoas})

def caixaExcluir(request, pk=0):
    try:
        caixa = Caixa.objects.get(pk=pk)
        caixa.delete()
        return HttpResponseRedirect('/caixas/')
    except:
        return HttpResponseRedirect('/caixas/')




    




