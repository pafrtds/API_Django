from django.shortcuts import render
from rest_framework import viewsets
from .models import Produto, Categoria
from .produtos import ProdutoSerializer, CategoriaSerializer

from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters  import rest_framework as filters

# Create your views here.

class ProdutoFilter(filters.FilterSet):

  class Meta:
    model = Produto
    fields = ('categoria',)

class ProdutoView(viewsets.ModelViewSet):
  queryset = Produto.objects.all()
  serializer_class = ProdutoSerializer
  filterset_class = ProdutoFilter

  @action(methods=['get'], detail=False)
  def newest(self, reques):
    newest = self.get_queryset().order_by('codigo').last()
    serializer = self.get_serializer_class()(newest)
    return Response(serializer.data)

class CategoriaView(viewsets.ModelViewSet):
  queryset = Categoria.objects.all()
  serializer_class = CategoriaSerializer

class ProdutoCategoriaView(viewsets.ModelViewSet):
  queryset = Produto.objects.filter(categoria=2)
  serializer_class = ProdutoView