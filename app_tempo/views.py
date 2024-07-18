import requests
from django.shortcuts import render
from .models import Cidade
from .forms import CidadeForm
from django.shortcuts import redirect

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=pt&appid=bcb1a47b4b6bd8b407948fe357982dab'

    if request.method == 'POST':            # Se houver um post, cria uma nova cidade do formulário.
        form = CidadeForm(request.POST)
        if form.is_valid():
            form.save()

    form = CidadeForm()                     # Cria uma instância vazia do formulário.
    cidades = Cidade.objects.all()          # Obtém todas as cidades salvas no banco de dados.
    dados_tempo = []

    for cidade in cidades:
        response = requests.get(url.format(cidade.nome)).json()
        print(f"Resposta da API para {cidade.nome}: {response}") # Depuração
        if response.get('cod') != 200:
            print(f"Erro ao obter dados para {cidade.nome}: {response.get('message')}")
            continue
        tempo = {                           # Formata os dados do clima para exibição.
            'cidade': cidade.nome,
            'temperatura': response['main']['temp'],
            'descricao': response['weather'][0]['description'],
            'icone': response['weather'][0]['icon']
        }
        dados_tempo.append(tempo)

    contexto = {'dados_tempo': dados_tempo, 'form': form}

    return render(request, 'app_tempo/index.html', contexto)

def limpar_cidades(request):                # Função para limpar todos os objetos de "Cidade" da página
    Cidade.objects.all().delete()
    return redirect('index')
