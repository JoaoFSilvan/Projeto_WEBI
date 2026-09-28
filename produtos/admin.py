from django.contrib import admin
from .models import Produto, Avaliacao


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'criado_em')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = (
        'produto',
        'usuario',
        'nota',
        'criado_em',
    )