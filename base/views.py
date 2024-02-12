from django.shortcuts import render
from base.models import Imovel
def lista_locacao(request):
    imoveis = Imovel.objects.filter(esta_locado=False)
    context = {
        'imoveis': imoveis
    }
    return render(request, 'lista-locacao.html', context)
