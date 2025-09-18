from django.contrib import admin
from .models import Noticia, CategoriaNoticia, TagNoticia, Comentario

# Registra os modelos no painel de administração do Django
admin.site.register(Noticia)
admin.site.register(CategoriaNoticia)
admin.site.register(TagNoticia)
admin.site.register(Comentario)