from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
# from django.urls import reverse

from erp.forms import FuncionarioForm
from erp.models import Funcionario


# Create your views here.
def home(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'erp/index.html')


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
  
