# imports
from django.urls import path 

# Importamos as views da nossa aplicação (o arquivo views.py)
from . import views          

# Define o "namespace" para a aplicação
app_name = 'estoque' 

urlpatterns = [
    # O caminho vazio '' significa a raiz da nossa aplicação 'produtos'
    path('', views.index, name='index'),
    path('teste/', views.teste, name='este'),

    ##
    # Produtos
    ##
    path('produtos/', views.ProdutoListView.as_view(), name='produto_list'), #dashboard
    path('produtos/listar/', views.ProdutoTabelaListView.as_view(), name='produto_tabela_list'), #produtos
    path('produtos/<int:pk>/', views.ProdutoDetailView.as_view(), name='produto_detail'),
    path('produtos/novo/', views.ProdutoCreateView.as_view(), name='produto_create'),
    path('produtos/<int:pk>/editar/', views.ProdutoUpdateView.as_view(), name='produto_update'),
    path('produtos/<int:pk>/deletar/', views.ProdutoDeleteView.as_view(), name='produto_delete'),

    path('categorias/', views.CategoriaListView.as_view(), name='categoria_list'), #dashboard
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria_detail'),
    path('categorias/<int:pk>/editar/', views.CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categoria/<int:pk>/deletar/', views.CategoriaDeleteView.as_view(), name='categoria_confirm_delete'),
    # path('categoria/<int:pk>/criar/', views.CategoriaCreateView.as_view(), name='categoria_create'),

    path('tags/', views.TagListView.as_view(), name='tag_list'),
    path('tags/novo/', views.TagCreateView.as_view(), name='tag_form'),           # criação
    path('tags/<int:pk>/editar/', views.TagUpdateView.as_view(), name='tag_update'),  # edição
    path('tags/<int:pk>/deletar/', views.TagDeleteView.as_view(), name='tag_delete'),
    path('tags/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),

]