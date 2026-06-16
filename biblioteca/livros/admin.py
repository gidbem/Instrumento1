from django.contrib import admin
from .models import Livros, Categoria, Disponivel

admin.site.register(Livros)
admin.site.register(Categoria)
admin.site.register(Disponivel)


