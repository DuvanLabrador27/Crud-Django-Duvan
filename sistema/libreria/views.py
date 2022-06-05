from django.shortcuts import render
from django.http import HttpResponse
from  .models import Libro
# Create your views here.

def inicio(request):
     return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros=Libro.objects.all()
    return render(request, 'libros/index.html', {'libros':libros})

def crearLibros(request):
    return render(request, 'libros/crearLibro.html')

def editarLibros(request):
    return render(request, 'libros/editarLibro.html')