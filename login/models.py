from django.db import models
from django.contrib.auth.models import AbstractUser
from camaras.models import Camara
from django_bunny.storage import BunnyStorage

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
import os
from django.conf import settings
from django.template.loader import render_to_string

class CustomUser(AbstractUser):

    foto_portada = models.URLField(default='https://staticurix.b-cdn.net/Default/Portada/portada_1.jpg')
    foto_perfil = models.URLField(default='https://staticurix.b-cdn.net/Default/Perfil/huasca.jpg')
    creditos = models.IntegerField(default= 0)
    
    fecha = models.DateField(auto_now_add=True)
    premium = models.CharField(max_length=250, default='free')
 
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios' 

    def __str__(self):
        return self.username

class Favorito(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='favoritos')
    fecha = models.DateField(auto_now_add=True)
    camara = models.ForeignKey(Camara, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'
        unique_together = ('usuario', 'camara')

    def __str__(self):
        return f'{self.usuario.username} - {self.camara.titulo}'

class Guardado(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='guardados')
    fecha = models.DateField(auto_now_add=True)
    camara = models.ForeignKey(Camara, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Guardado'
        verbose_name_plural = 'Guardados'
        unique_together = ('usuario', 'camara')

    def __str__(self):
        return f'{self.usuario.username} - {self.camara.titulo}'

class Idea(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete= models.CASCADE, related_name='ideas')
    descripcion = models.TextField(max_length = 2500)
    imagen = models.ImageField(storage=BunnyStorage(), upload_to='ideas/')

    class Meta:
        verbose_name = 'Idea'
        verbose_name_plural = 'Ideas'

    def __str__(self):
        return f'{self.usuario.username} - {self.descripcion[:30]}'

class Comentario(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comentarios')
    text = models.TextField(max_length=10000)
    fecha = models.DateTimeField(auto_now_add=True)
    puntuacion = models.FloatField()
    imagen = models.ImageField(storage=BunnyStorage(), upload_to='comentarios/', blank=True, null=True)
    status = models.BooleanField(default=True)
 
    # Estos campos son necesarios para la relación genérica
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return f'{self.user.username} - {str(self.puntuacion)}'


class ImagenesDefault(models.Model):
    def cliente_logo_path(instance, filename):
     
        return f'Default/{instance.tipo}/{filename}'
    tipo = models.CharField(max_length=50)
    imagen = models.ImageField(storage=BunnyStorage(), upload_to=cliente_logo_path)
    acceso = models.CharField(max_length=50, default='free')
    def __str__(self) -> str:
        return str(self.tipo +' '+self.imagen.name)

from django.core.mail import send_mail


class Contacto(models.Model):
    correo_cliente = models.CharField(max_length=250)
    asunto = models.CharField(max_length=500)
    estado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    responsable = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    mensaje = models.TextField()
        
    def enviar_correo(self):
        try:
            # Renderiza la plantilla HTML con los datos específicos
            context = {'nombre': 'Juan', 'mensaje_personalizado': '¡Hola!'}
            html_message = render_to_string('login/contacto/plantilla_envio.html', context)

            # Envía el correo con la plantilla HTML
            send_mail(self.asunto, '', settings.EMAIL_HOST_USER, [self.correo_cliente], html_message=html_message)
            return True, 'success'
        except Exception as e:
            return False, str(e)
        
        
        
class Atencion(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    nombres = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    telefono = models.CharField(max_length=250)
    mensaje = models.TextField()
    motivo = models.CharField(max_length=250)
    estado = models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return self.nombres
    
    