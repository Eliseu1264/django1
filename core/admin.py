from django.contrib import admin

from .models import Produtos, Clientes

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade')
    
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'email', 'celular')

admin.site.register(Produtos, ProdutoAdmin)
admin.site.register(Clientes, ClienteAdmin)