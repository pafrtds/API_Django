from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('produtos',views.ProdutoView)
router.register('categoria',views.CategoriaView)

#router.register('produtos/categoria',views.ProdutoCategoriaView)

urlpatterns = [
  path('',include(router.urls))
]