from django.db import models

class Produtos(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    quantidade = models.IntegerField("Quantidade")
    
class Clientes(models.Model):
    nome = models.CharField('Nome', max_length=100)
    endereco = models.CharField('Endereço', max_length=100)
    email = models.EmailField('Email')
    celular = models.CharField('Celjlar', max_length=11)