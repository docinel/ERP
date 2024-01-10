from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView, DeleteView
from erp.forms import FuncionarioForm, ProdutoForm
from erp.models import Funcionario, Produto, Venda
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# def home(request: HttpRequest):
#     if request.method == 'GET':
#         return render(request, 'erp/index.html')


class ErpLoginView(LoginView):
    template_name = 'erp/login.html'
    success_url = reverse_lazy('erp:dashboard')
    redirect_authenticated_user = True


class ErpLogoutView(LogoutView):
    template_name = 'erp/logout.html'


class HomeView(TemplateView):
    template_name = 'erp/index.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'erp/dashboard.html'


@login_required
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


@login_required
def lista_funcionarios(request: HttpRequest):
    if request.method == 'GET':
        funcionarios = Funcionario.objects.all()

        return render(request, 'erp/funcionarios/lista.html', {'funcionarios': funcionarios})


@login_required
def busca_funcionario_por_id(request: HttpRequest, pk: int):
    if request.method == 'GET':
        try:
            funcionario = Funcionario.objects.get(id=pk)
        except Funcionario.DoesNotExist:
            funcionario = None

        return render(request, 'erp/funcionarios/detalhe.html', {'funcionario': funcionario})


@login_required
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


class ProdutoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'erp/produtos/novo.html'
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('erp:cria_produto')


class ProdutoListView(LoginRequiredMixin, ListView):
    template_name = 'erp/produtos/lista.html'
    model = Produto
    context_object_name = 'produtos'


class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'erp/produtos/atualiza.html'
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('erp:lista_produtos')


class ProdutoDetailView(LoginRequiredMixin, DetailView):
    template_name = 'erp/produtos/detalhe.html'
    model = Produto
    context_object_name = 'produto'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None


class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'erp/produtos/deleta.html'
    context_object_name = 'produto'
    success_url = reverse_lazy('erp:lista_produtos')

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None


class VendaCreateView(LoginRequiredMixin, CreateView):
    model = Venda
    template_name = 'erp/vendas/novo.html'
    success_url = reverse_lazy('erp:cria_venda')
    fields = ['funcionario', 'produto']


class VendaListView(LoginRequiredMixin, ListView):
    model = Venda
    template_name = 'erp/vendas/lista.html'
    context_object_name = 'vendas'


class VendaDetailView(LoginRequiredMixin, DetailView):
    model = Venda
    template_name = 'erp/vendas/detalhe.html'
    context_object_name = 'venda'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None


class VendaUpdateView(LoginRequiredMixin, UpdateView):
    model = Venda
    template_name = 'erp/vendas/atualiza.html'
    fields = '__all__'
    success_url = reverse_lazy('erp:lista_vendas')


class VendaDeleteView(LoginRequiredMixin, DeleteView):
    model = Venda
    template_name = 'erp/vendas/deleta.html'
    context_object_name = 'venda'
    success_url = reverse_lazy('erp:lista_vendas')

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None
