from django.shortcuts import render
from django.http.response import HttpResponse
from calc.src.ArbolDeExpresiones import *


def calcular(request):
    if request.method == 'POST':
        expresion = request.POST['expresion']  
        a = infijaAPostfija(expresion)
        arbol = ArbolDeExpresiones()
        raiz = arbol.constructTree(a)
        resulado = arbol.calcular(raiz)

        return render(request, 'index.html', {'exp':expresion,'res': resulado,'pos':a})

    return render(request, 'index.html')
    





