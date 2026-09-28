from django import forms
from .models import Produto, Avaliacao


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco']


class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nota', 'comentario']

    def clean_nota(self):
        nota = self.cleaned_data['nota']

        if nota < 1 or nota > 5:
            raise forms.ValidationError(
                'A nota deve estar entre 1 e 5.'
            )

        return nota