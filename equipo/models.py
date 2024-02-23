from django.db import models
from django_bunny.storage import BunnyStorage

# Create your models here.
class Personal(models.Model):
    nombre = models.CharField(max_length=250)
    apellidom = models.CharField(max_length=250)
    apellidop = models.CharField(max_length=250)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=250)
    descripcion = models.TextField(max_length=10000)
    mison = models.TextField(max_length=10000, null=True , blank=True)
    vision = models.TextField(max_length=10000, null=True , blank=True)
    puesto = models.CharField(max_length=250, null=True , blank=True)
    foto_perfil = models.ImageField(storage=BunnyStorage(), upload_to='perfil_personal/',null=True,blank=True)
    foto_portada = models.ImageField(storage=BunnyStorage(),upload_to='portada_personal/',null=True,blank=True)

    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personal'

    def __str__(self):
        return self.nombre