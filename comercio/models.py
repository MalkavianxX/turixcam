from django.db import models
import os
from django_bunny.storage import BunnyStorage

# Create your models here.
class Comercio(models.Model):

    def cliente_logo_path(instance, filename):
        # Conservar la extensión del archivo original
        extension = os.path.splitext(filename)[1]
        # Construir la ruta con el nombre del cliente y el archivo
        return f'Clientes/{instance.cliente}/logo/{instance.cliente}_logo{extension}'

    def cliente_portada_path(instance, filename):
        # Conservar la extensión del archivo original
        extension = os.path.splitext(filename)[1]
        # Construir la ruta con el nombre del cliente y el archivo
        return f'Clientes/{instance.cliente}/portada/{instance.cliente}_portada{extension}'
    def cliente_qr_path(instance, filename):
        # Conservar la extensión del archivo original
        extension = os.path.splitext(filename)[1]
        # Construir la ruta con el nombre del cliente y el archivo
        return f'Clientes/{instance.cliente}/qrs/{instance.cliente}_qr{extension}'

    cliente = models.CharField(max_length=200)
    estrellas = models.IntegerField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    logo = models.ImageField(storage=BunnyStorage(),upload_to=cliente_logo_path,null=True, blank=True)
    portada = models.ImageField(storage=BunnyStorage(),upload_to=cliente_portada_path,null=True, blank=True)

    tipo = models.CharField(max_length=200)
    plan = models.CharField(max_length=200)
    importancia = models.IntegerField()
    detalles = models.TextField()

    camara = models.CharField(max_length=80, default='Ninguna')
    apertura = models.TimeField()
    cierre = models.TimeField()
    resumen = models.TextField()


    qr = models.ImageField(storage=BunnyStorage(),upload_to=cliente_qr_path,null=True, blank=True)


    estado = models.BooleanField(default=True)
    fecha = models.DateField(auto_now_add=True)


class Imagen(models.Model):
    def cliente_galeria_path(instance, filename):
        # Construir la ruta con el nombre del cliente y el archivo
        return f'Clientes/{instance.comercio.cliente}/galeria/{filename}'
    comercio = models.ForeignKey(Comercio, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(storage=BunnyStorage(), upload_to=cliente_galeria_path, null=True, blank=True)

