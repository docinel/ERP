from django.db import models

# Create your models here.

# ENTIDADE: FUNCIONÁRIO
# Campos:
#   - Nome
#   - Sobrenome
#   - CPF
#   - Email funcional
#   - Remuneração


class Funcionario(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)
    sobrenome = models.CharField(max_length=70, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    remuneracao = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)


# ENTIDADE: PRODUTO
# Campos:
#   - Nome
#   - Descricção
#   - Preço


class Produto(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.CharField(max_length=255, null=False, blank=False)
    preco = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)


# ENTIDADE: VENDA
# Campos:
#   - Funcionário
#   - Produto
#   - Data/hora


class Venda(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
