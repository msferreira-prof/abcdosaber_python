from django.shortcuts import render

# Create your views here.
def listar(request):
    lista_titulos = Titulo.objects.all()
    contexto = {
        'titulos': lista_titulos
    }
    return render(request, 'titulo/listarTitulos.html', context=contexto)

