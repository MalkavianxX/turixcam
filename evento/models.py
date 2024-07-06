from django.db import models
from login.models import CustomUser
from camaras.models import Camara, Stream
import os
from django_bunny.storage import BunnyStorage

class Evento(models.Model):
    titulo = models.CharField(max_length=2500)
    descripcion = models.TextField(max_length=2500)
    url_accion = models.URLField(max_length=2500)
    fecha_inicio = models.DateTimeField()
    fecha_cierre = models.DateTimeField()

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
 
class Notificacion(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notificaciones')
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='notificaciones')
    visto = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Notificación'
        verbose_name_plural = 'Notificaciones'
        unique_together = ('usuario', 'evento',)


class EventoCultural(models.Model):
    def camara_logo_path(instance, filename):
        # Conservar la extensión del archivo original
        extension = os.path.splitext(filename)[1]
        # Construir la ruta con el nombre del titulo y el archivo
        return f'Eventos/{instance.titulo}/logos/{instance.titulo}_logo{extension}'
    
    COBERTURA = {
        'No': 'Sin cobertura',
        'Si': 'Con cobertura',
        # Agrega más opciones según tus necesidades
    } 

    titulo = models.CharField(max_length=250)
    fecha_inicio = models.DateTimeField()
    fecha_cierre = models.DateTimeField()
    direccion = models.TextField()
    estado = models.CharField(max_length=250)
    municipio = models.CharField(max_length=250)
    camara = models.ForeignKey(Camara, on_delete=models.CASCADE, blank=True, null=True)
    logo = models.ImageField(storage=BunnyStorage(), upload_to=camara_logo_path, null=True, blank=True, max_length=250)
    detalles = models.TextField()
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, null=True, blank=True)
    cobertura = models.CharField(max_length=50, choices=COBERTURA, default='Si')
    
    promocion = models.IntegerField(default=0)
    espectadores = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.titulo

    class Meta:

        verbose_name = 'Evento cultural'
        verbose_name_plural = 'Eventos culturales'
        
        
        
class Imagen(models.Model):
    def evento_galeria_path(instance, filename):
        # Construir la ruta con el nombre del cliente y el archivo
        return f'Eventos/{instance.evento.titulo}/galeria/{filename}'
    
    evento = models.ForeignKey(EventoCultural, related_name='images', on_delete=models.CASCADE)
    imagen = models.ImageField(storage=BunnyStorage(), upload_to=evento_galeria_path, null=True, blank=True)