from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView, DeleteView
from erp.forms import FuncionarioForm, ProdutoForm
from erp.models import Funcionario, Produto, Venda


# Create your views here.
# def home(request: HttpRequest):
#     if request.method == 'GET':
#         return render(request, 'erp/index.html')

class HomeView(TemplateView):
    template_name = 'erp/index.html'


def cria_funcionario(request: HttpRequest):
    if request.method == 'GET':
        form = FuncionarioForm()

        return render(request, 'erp/funcionarios/novo.html', {'form': form})
    elif request.method == 'POST':
        form = FuncionarioForm(request.POST)

        if form.is_valid():
            funcionario = Funcionario(**form.cleaned_data)  # Desempacotamento
            """ nome=form.cleaned_data.get('nome'),
                sobrenome=form.cleaned_data.get('sobrenome'),
                cpf=form.cleaned_data.get('cpf'),
                email_funcional=form.cleaned_data.get('email_funcional'),
                remuneracao=form.cleaned_data.get('remuneracao') """

            funcionario.save()

            return HttpResponseRedirect(redirect_to='/')


def lista_funcionarios(request: HttpRequest):
    if request.method == 'GET':
        funcionarios = Funcionario.objects.all()

        return render(request, 'erp/funcionarios/lista.html', {'funcionarios': funcionarios})


def busca_funcionario_por_id(request: HttpRequest, pk: int):
    if request.method == 'GET':
        try:
            funcionario = Funcionario.objects.get(id=pk)
        except Funcionario.DoesNotExist:
            funcionario = None

        return render(request, 'erp/funcionarios/detalhe.html', {'funcionario': funcionario})


def atualiza_funcionario(request: HttpRequest, pk: int):
    if request.method == 'GET':
        funcionario = Funcionario.objects.get(pk=pk)
        form = FuncionarioForm(instance=funcionario)

        return render(request, 'erp/funcionarios/atualiza.html', {'form': form})

    elif request.method == 'POST':
        funcionario = Funcionario.objects.get(pk=pk)
        form = FuncionarioForm(request.POST, instance=funcionario)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(redirect_to=f'/funcionarios/detalhe/{pk}')


class ProdutoCreateView(CreateView):
    template_name = 'erp/produtos/novo.html'
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('erp:cria_produto')


class ProdutoListView(ListView):
    template_name = 'erp/produtos/lista.html'
    model = Produto
    context_object_name = 'produtos'


class ProdutoUpdateView(UpdateView):
    template_name = 'erp/produtos/atualiza.html'
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('erp:lista_produtos')


class ProdutoDetailView(DetailView):
    template_name = 'erp/produtos/detalhe.html'
    model = Produto
    context_object_name = 'produto'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None


class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'erp/produtos/deleta.html'
    context_object_name = 'produto'
    success_url = reverse_lazy('erp:lista_produtos')

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None


class VendaCreateView(CreateView):
    model = Venda
    template_name = 'erp/vendas/novo.html'
    success_url = reverse_lazy('erp:cria_venda')
    fields = ['funcionario', 'produto']


class VendaListView(ListView):
    model = Venda
    template_name = 'erp/vendas/lista.html'
    context_object_name = 'vendas'


class VendaDetailView(DetailView):
    model = Venda
    template_name = 'erp/vendas/detalhe.html'
    context_object_name = 'venda'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None


class VendaUpdateView(UpdateView):
    model = Venda
    template_name = 'erp/vendas/atualiza.html'
    fields = '__all__'
    success_url = reverse_lazy('erp:lista_vendas')


class VendaDeleteView(DeleteView):
    model = Venda
    template_name = 'erp/vendas/deleta.html'
    context_object_name = 'venda'
    success_url = reverse_lazy('erp:lista_vendas')

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None
