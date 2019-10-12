from rest_framework import serializers
from .models import Produto, Categoria

class ProdutoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Produto
    fields = ('codigo','descricao','preco','categoria','ncm','icms','ip','src','sefaz')

class CategoriaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Categoria
    fields = ('codigo','descricao','src')