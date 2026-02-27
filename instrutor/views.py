# Create your views here.
from urllib import request
from django.shortcuts import render
from instrutor.forms import InstrutorForm
from instrutor.models import Instrutor
from titulo.models import Titulo

# Create your views here.
## listar os instrutores cadastrados
def listar(request):
    lista_instrutor = Instrutor.objects.all()
    contexto = {
        'instrutores': lista_instrutor,
    }
    return render(request, 'instrutor/listarInstrutores.html', context=contexto)

## carregar a pagina de cadastro de instrutor
def carregar_cadastro(request):
    lista_titulos = Titulo.objects.all()
    contexto = {
        'titulos': lista_titulos,
    }

    return render(request, 'instrutor/cadastroInstrutor.html', context=contexto)

## cadastrar um instrutor
def cadastrar(request):
    form = InstrutorForm(request.POST)
    if form.is_valid():
        dados_instrutor = form.cleaned_data
        instrutor = Instrutor(
            nome=dados_instrutor['nome'],
            rg=dados_instrutor['rg'],
            data_nascimento=dados_instrutor['data_nascimento'],
            ddd=dados_instrutor['ddd'],
            telefone=dados_instrutor['telefone'],
            codigo_titulo=dados_instrutor['codigo_titulo']
        )
        
        instrutor.save()
    
        return render(request, 'instrutor/cadastroInstrutor.html')
    
    else:
        erros = form.errors
        contexto = {
            'erros': erros,
        }

        return render(request, 'instrutor/pagina_erro.html', context=contexto)
