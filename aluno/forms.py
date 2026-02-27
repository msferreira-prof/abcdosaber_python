from django import forms

# Create your models here.
class AlunoForm(forms.Form):
    nome = forms.CharField(max_length=70, help_text='Informe o nome do aluno')
    data_inicial = forms.DateField(help_text='Informe a data inicial de matrícula do aluno')
    data_final = forms.DateField(help_text='Informe a data de final de matrícula do aluno')
