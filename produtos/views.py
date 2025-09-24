from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ver_produto(request):
    return render(request, 'ver_produto.html', {'nome' : 'Anderson'})

def inserir_produtos(request):
    return HttpResponse("Olá inserir produto")
