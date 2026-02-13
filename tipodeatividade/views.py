from urllib import request
from django.shortcuts import render
from tipodeatividade.models import TipoDeAtividade
from tipodeatividade.forms import TipoDeAtividadeForm

# Create your views here.
## listar os tipos de atividade cadastrados
def listar(request):
    lista_tipodeatividade = TipoDeAtividade.objects.all()
    contexto = {
        'tiposdeatividade': lista_tipodeatividade,
    }
    return render(request, 'tipodeatividade/listarTiposAtividade.html', context=contexto)

## carregar a pagina de cadastro de tipo de atividade
def carregar_cadastro(request):
    return render(request, 'tipodeatividade/cadastroTipoDeAtividade.html')

## cadastrar um tipo de atividade
def cadastrar(request):
    form = TipoDeAtividadeForm(request.POST)
    if form.is_valid():
        dados_tipodeatividade = form.cleaned_data
        tipodeatividade = TipoDeAtividade(
            descricao=dados_tipodeatividade['descricao']
        )
        
        tipodeatividade.save()
        
    return render(request, 'tipodeatividade/cadastroTipoDeAtividade.html')
