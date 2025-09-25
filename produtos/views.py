from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoas

# Create your views here.

def ver_produto(request):
    if request.method == 'GET':
       return render(request, 'ver_produto.html', {'nome' : 'Anderson'})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        pessoas = Pessoas(nome = nome, idade = idade)
        pessoas.save()

        return HttpResponse("Fui chamdado")


def inserir_produtos(request):
    return HttpResponse("Olá inserir produto")
