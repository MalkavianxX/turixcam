from django.db import models
from django_bunny.storage import BunnyStorage
import os
class Stream(models.Model):
    url = models.URLField(max_length=2500)
    key = models.CharField(max_length=2500)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Stream'
        verbose_name_plural = 'Streams'

    def __str__(self): 
        return self.url

class Camara(models.Model):
    def camara_background_path(instance, filename):
        # Conservar la extensión del archivo original
        extension = os.path.splitext(filename)[1]
        # Construir la ruta con el nombre del titulo y el archivo
        return f'Camaras/{instance.titulo}/background/{instance.titulo}_background{extension}'
    def camara_background_dark_path(instance, filename):
        # Conservar la extensión del archivo original
        extension = os.path.splitext(filename)[1]
        # Construir la ruta con el nombre del titulo y el archivo
        return f'Camaras/{instance.titulo}/backgrounDark/{instance.titulo}_backgroundDark{extension}'

    def camara_logo_path(instance, filename):
        # Conservar la extensión del archivo original
        extension = os.path.splitext(filename)[1]
        # Construir la ruta con el nombre del titulo y el archivo
        return f'Camaras/{instance.titulo}/logo/{instance.titulo}_logo{extension}'
    
    def camara_pin_path(instance, filename):
        # Conservar la extensión del archivo original
        extension = os.path.splitext(filename)[1]
        # Construir la ruta con el nombre del titulo y el archivo
        return f'Camaras/{instance.titulo}/pin/{instance.titulo}_pin{extension}'


    titulo = models.CharField(max_length=250)
    estado = models.CharField(max_length=250)
    municipio = models.CharField(max_length=250)
    background =models.ImageField(storage=BunnyStorage(), upload_to=camara_background_path, null=True, blank=True)
    background_dark =models.ImageField(storage=BunnyStorage(), upload_to=camara_background_dark_path, null=True, blank=True)
    background_web =models.ImageField(storage=BunnyStorage(), upload_to=camara_background_path, null=True, blank=True)
    background_dark_web =models.ImageField(storage=BunnyStorage(), upload_to=camara_background_dark_path, null=True, blank=True)
    camdisp = models.BooleanField(default=True)
    createdAt = models.IntegerField(default=0)
    descripcion = models.TextField()
    etiquetauno = models.TextField()
    etiquetados = models.TextField()
    etiquetatres = models.TextField()
    etiquetacuatro = models.TextField()
    logo = models.ImageField(storage=BunnyStorage(), upload_to=camara_logo_path)
    latitude = models.CharField(max_length=250)
    longitude = models.CharField(max_length=250)
    likes = models.IntegerField(default=0)
    pin = models.ImageField(storage=BunnyStorage(), upload_to=camara_background_path)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, related_name='streams', null=True, blank=True)

    class Meta:
        verbose_name = 'Camara'
        verbose_name_plural = 'Camaras'

    def __str__(self):
        return self.titulo
    

