from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


class Produto(models.Model):
    nome = models.CharField(max_length=200)

    descricao = models.TextField()

    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nome

    @property
    def media_avaliacoes(self):
        media = self.avaliacoes.aggregate(
            media=Avg('nota')
        )['media']

        return media or 0


class Avaliacao(models.Model):

    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        related_name='avaliacoes'
    )

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    nota = models.PositiveIntegerField()

    comentario = models.TextField(
        blank=True
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['produto', 'usuario'],
                name='avaliacao_unica_por_usuario'
            )
        ]

    def __str__(self):
        return f'{self.usuario.username} - {self.produto.nome}'