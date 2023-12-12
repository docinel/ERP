from django import forms

from erp.models import Funcionario


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'sobrenome', 'cpf', 'email_funcional', 'remuneracao']

    """ nome = forms.CharField(max_length=30, required=True)
    sobrenome = forms.CharField(max_length=70, required=True)
    cpf = forms.CharField(max_length=14, required=True)
    email_funcional = forms.EmailField(max_length=100, required=True)
    remuneracao = forms.DecimalField(max_digits=8, decimal_places=2, required=True) """
