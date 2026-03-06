from urllib import request
from django.shortcuts import redirect, render
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

## excluir um tipo de atividade
def excluir(request, codigo):
    try:
        tipodeatividade = TipoDeAtividade.objects.get(pk=codigo)
        tipodeatividade.delete()
    except TipoDeAtividade.DoesNotExist:
        pass
    
    # a função redirect é utilizada para redirecionar o usuário para uma URL, 
    # e não para renderizar um template, como a função render. 
    # Por isso, a função redirect é mais adequada para ser utilizada em casos de exclusão de registros, 
    # onde o usuário deve ser redirecionado para a página de listagem de registros após a exclusão do registro. 
    # Já a função render é mais adequada para ser utilizada em casos de cadastro e atualização de registros,
    # onde o usuário deve permanecer na mesma página após a realização da ação. 
    return redirect('tipodeatividade:listar')
