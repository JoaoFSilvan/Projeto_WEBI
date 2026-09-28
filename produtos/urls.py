from django.urls import path

from .views import (
    ProdutoListView,
    ProdutoDetailView,
    ProdutoCreateView,
    ProdutoUpdateView,
    ProdutoDeleteView,
    AvaliacaoCreateView,
)


urlpatterns = [
    path('', ProdutoListView.as_view(), name='produto-list'),

    path(
        'produto/<int:pk>/',
        ProdutoDetailView.as_view(),
        name='produto-detail'
    ),

    path(
        'produto/novo/',
        ProdutoCreateView.as_view(),
        name='produto-create'
    ),

    path(
        'produto/<int:pk>/editar/',
        ProdutoUpdateView.as_view(),
        name='produto-update'
    ),

    path(
        'produto/<int:pk>/excluir/',
        ProdutoDeleteView.as_view(),
        name='produto-delete'
    ),

    path(
    'produto/<int:pk>/avaliar/',
    AvaliacaoCreateView.as_view(),
    name='avaliacao-create'
),

]