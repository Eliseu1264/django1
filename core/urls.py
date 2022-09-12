from django.urls import path
from .views import f_index, f_contato, f_produto, f_cliente

urlpatterns = [
    path('', f_index, name='index'),
    path('contato/', f_contato, name='contato'),
    path('produto/<int:pk>', f_produto, name='produto'),
    path('cliente/<int:pk>', f_cliente, name='cliente'),
]