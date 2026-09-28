from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Produto, Avaliacao
from .forms import ProdutoForm, AvaliacaoForm


class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/produto_list.html'
    context_object_name = 'produtos'
    paginate_by = 6


class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produtos/produto_detail.html'
    context_object_name = 'produto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        usuario = self.request.user

        if usuario.is_authenticated:
            context['ja_avaliou'] = Avaliacao.objects.filter(
                produto=self.object,
                usuario=usuario
            ).exists()
        else:
            context['ja_avaliou'] = False

        return context


class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtos/produto_form.html'
    success_url = reverse_lazy('produto-list')


class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtos/produto_form.html'
    success_url = reverse_lazy('produto-list')


class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'produtos/produto_confirm_delete.html'
    success_url = reverse_lazy('produto-list')


class AvaliacaoCreateView(LoginRequiredMixin, CreateView):
    model = Avaliacao
    form_class = AvaliacaoForm
    template_name = 'produtos/avaliacao_form.html'

    def dispatch(self, request, *args, **kwargs):
        produto = get_object_or_404(Produto, pk=kwargs['pk'])

        if request.user.is_authenticated:
            ja_avaliou = Avaliacao.objects.filter(
                produto=produto,
                usuario=request.user
            ).exists()

            if ja_avaliou:
                return redirect('produto-detail', pk=produto.pk)

        self.produto = produto
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.produto_id = self.kwargs['pk']

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'produto-detail',
            kwargs={'pk': self.kwargs['pk']}
        )