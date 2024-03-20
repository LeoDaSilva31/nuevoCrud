from django.shortcuts import render

def bienvenida(request):
    return render(request, 'bienvenida.html')

def cargar(request):
    return render(request, 'cargar.html')

def buscar(request):
    return render(request, 'buscar.html')

def editar(request):
    return render(request, 'editar.html')

def estadisticas(request):
    return render(request, 'estadisticas.html')

