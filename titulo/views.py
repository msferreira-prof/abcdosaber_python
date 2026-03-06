from django.shortcuts import render, redirect
from titulo.models import Titulo
from titulo.forms import TituloForm

# Create your views here.
def listar(request):
    lista_titulos = Titulo.objects.all()
    contexto = {
        'titulos': lista_titulos
    }
    return render(request, 'titulo/listarTitulos.html', context=contexto)

## carregar a pagina de cadastro de titulo
def carregar_cadastro(request):
    return render(request, 'titulo/cadastroTitulo.html')

## cadastrar um titulo
def cadastrar(request):
    form = TituloForm(request.POST)
    if form.is_valid():
        dados_titulo = form.cleaned_data
        titulo = Titulo(
            descricao=dados_titulo['descricao']
        )
        
        titulo.save()
        
    return render(request, 'titulo/cadastroTitulo.html')

## excluir um tipo de atividade
def excluir(request, codigo):
    try:
        titulo = Titulo.objects.get(pk=codigo)
        titulo.delete()
    except Titulo.DoesNotExist:
        pass
    
    return redirect('titulo:listar')