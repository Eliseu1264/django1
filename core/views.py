from multiprocessing import context
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def contato(request):
    dados = {
        'nome': 'EBL',
        'curso': 'Aprendendo Django',
        'data': '10/09/2022'
    }
    return render(request, 'contato.html', dados)