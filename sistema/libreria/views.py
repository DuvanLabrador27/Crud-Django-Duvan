from django.shortcuts import redirect, render
from django.http import HttpResponse
from  .models import Libro
from .forms import LibroForm
# Create your views here.

def inicio(request):
     return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    #Obtener todos los libros (LISTAR)
    libros=Libro.objects.all()
    return render(request, 'libros/index.html', {'libros':libros})

def crearLibros(request):
    formulario=LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crearLibro.html', {'formulario':formulario})

def editarLibros(request,id):
    libro=Libro.objects.get(id=id)
    formulario=LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editarLibro.html', {'formulario':formulario})

def eliminarLibro(request,id):
    libro=Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')
