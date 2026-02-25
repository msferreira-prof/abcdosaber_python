from django import forms

# Create your models here.
class InstrutorForm(forms.Form):
    rg = forms.CharField(max_length=15,  help_text='Informe o RG do instrutor')
    nome = forms.CharField(max_length=70, help_text='Informe o nome do instrutor')
    data_nascimento = forms.DateField(help_text='Informe a data de nascimento do instrutor')
    telefone = forms.CharField(max_length=9, help_text='Informe o telefone do instrutor')
    ddd = forms.CharField(max_length=3, help_text='Informe o DDD do telefone do instrutor')
    codigo_titulo = forms.IntegerField(help_text='Informe o código do título do instrutor')
