from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns=[
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/crearLibros', views.crearLibros, name='crearLibros'),
    path('libros/editarLibros', views.editarLibros, name='editarLibros'),
    path('eliminarLibro/<int:id>', views.eliminarLibro, name='eliminarLibro'),
    path('libros/editarLibros/<int:id>', views.editarLibros, name='editarLibros'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)