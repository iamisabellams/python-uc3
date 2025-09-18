from django.contrib import admin
from .models import Produto, CategoriaProduto, Marca, Tag

admin.site.register(Produto)
admin.site.register(CategoriaProduto)
admin.site.register(Marca)
admin.site.register(Tag)