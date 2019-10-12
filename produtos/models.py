from django.db import models

# Create your models here.


class Categoria(models.Model):
  codigo = models.IntegerField(primary_key=True,max_length=8)
  descricao = models.CharField(max_length=250)
  src = models.CharField(max_length=600, blank=True)
  def __str__(self):
    return self.descricao

class Produto(models.Model):
  codigo = models.IntegerField(primary_key=True,max_length=8)
  descricao = models.CharField(max_length=250)
  preco = models.DecimalField(max_digits=100,decimal_places=2)
  categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
  ncm = models.CharField(max_length=50)
  icms = models.CharField(max_length=2)
  ip = models.CharField(max_length=3)
  src = models.CharField(max_length=250)
  sefaz = models.CharField(max_length=250,blank=True)

