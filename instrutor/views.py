# Create your views here.
from urllib import request
from django.shortcuts import render
from instrutor.models import Instrutor

# Create your views here.
## listar os tipos de atividade cadastrados
def listar(request):
    lista_instrutor = Instrutor.objects.all()
    contexto = {
        'instrutores': lista_instrutor,
    }
    return render(request, 'instrutor/listarInstrutores.html', context=contexto)
