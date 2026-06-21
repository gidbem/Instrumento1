from django.contrib import admin
from .models import Livro, Categoria, Tag

class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'data_retirada', 'devolucao')
    readonly_fields = ('devolucao',)
    filter_horizontal = ('tags',)


admin.site.register(Categoria)
admin.site.register(Tag)
admin.site.register(Livro, LivroAdmin)


