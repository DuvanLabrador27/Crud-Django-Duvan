from django.db import models

# Create your models here.
class Libro(models.Model):
    id=models.AutoField(primary_key=True)
    titulo= models.CharField(max_length=100)
    imagen= models.ImageField(upload_to='imagenes/', null=True, blank=True)
    descripcion= models.TextField(verbose_name='Descripcion', null=True)

    def  __str__(self):
     return str(self.titulo)
    
    def  delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
