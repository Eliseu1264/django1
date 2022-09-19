from django.shortcuts import render
from core.models import Produtos, Clientes

def index(request):
    produtos = Produtos.objects.all()
    context = {'produtostb': produtos}
    return render(request, 'index.html', context)

def produto(request, pk):
    produtos = Produtos.objects.get(id=pk)
    context = {
        'nome': produtos.nome,
        'preco': produtos.preco,
        'quantidade': produtos.quantidade
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