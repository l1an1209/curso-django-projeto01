from django.shortcuts import render
from .models import Receita

# View para a página inicial
def home(request):
    return render(request, 'recipes/pages/home.html')

# View para listar receitas
def lista_receitas(request):
    receitas = Receita.objects.all().order_by('-data_publicacao')
    return render(request, 'recipes/pages/lista_receitas.html', {'receitas': receitas})
