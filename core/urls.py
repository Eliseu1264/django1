from distutils import core
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('contato/', views.f_contato, name='contato'),
    path('produto/<int:pk>', views.produto, name='produto'),
    path('cliente/<int:pk>', views.f_cliente, name='cliente'),
]