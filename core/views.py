from multiprocessing import context
from django.shortcuts import render
from core.models import Produtos, Clientes

def f_index(request):
    return render(request, 'index.html')

def f_produto(request, pk):
    prod = Produtos.objects.get(id=pk)
    context = {
        'd_produto': prod
    }
    return render(request, 'produto.html', context)

def f_cliente(request, pk):
    clie = Clientes.objects.get(id=pk)
    context = {
        'd_cliente': clie
    }
    return render(request, 'cliente.html', context)

def f_contato(request):
    dados = {
        'nome': 'EBL',
        'curso': 'Aprendendo Django',
        'data': '10/09/2022'
    }
    return render(request, 'contato.html', dados)