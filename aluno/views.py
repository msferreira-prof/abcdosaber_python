from django.shortcuts import render
from aluno.forms import AlunoForm
from aluno.models import Aluno

# Create your views here.
## listar os alunos cadastrados
def listar(request):
    lista_alunos = Aluno.objects.all()
    contexto = {
        'alunos': lista_alunos,
    }
    return render(request, 'aluno/listarAlunos.html', context=contexto)

## carregar a pagina de cadastro de aluno
def carregar_cadastro(request):
    return render(request, 'aluno/cadastroAluno.html')

## cadastrar um aluno
def cadastrar(request):
    form = AlunoForm(request.POST)
    if form.is_valid():
        dados_aluno = form.cleaned_data
        aluno = Aluno(
            nome=dados_aluno['nome'],
            data_inicial=dados_aluno['data_inicial'],
            data_final=dados_aluno['data_final']
        )
        
        aluno.save()
    else:
        print(form.errors)
    
    return render(request, 'aluno/cadastroAluno.html')
    