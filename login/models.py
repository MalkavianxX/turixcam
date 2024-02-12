from django.db import models
from django.contrib.auth.models import AbstractUser
from camaras.models import Lugar
from django_bunny.storage import BunnyStorage

class CustomUser(AbstractUser):
    foto_portada = models.ImageField(storage=BunnyStorage(),upload_to='fotos_portada/',null=True,blank=True)
 
    foto_perfil = models.ImageField(storage=BunnyStorage(), upload_to='fotos_perfil/',null=True,blank=True)
    custom_avatar_uploaded = models.BooleanField(default=False)
    horas = models.FloatField(default=0.0)
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.username

class Favorito(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='favoritos')
    fecha = models.DateField(auto_now_add=True)
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'
        unique_together = ('usuario', 'lugar',)

    def __str__(self):
        return f'{self.usuario.username} - {self.lugar.titulo}'

class Guardado(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='guardados')
    fecha = models.DateField(auto_now_add=True)
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Guardado'
        verbose_name_plural = 'Guardados'
        unique_together = ('usuario', 'lugar',)

    def __str__(self):
        return f'{self.usuario.username} - {self.lugar.titulo}'

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
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='comentarios')
    text = models.TextField(max_length = 10000)
    lugar = models.ForeignKey(Lugar, on_delete = models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    puntuacion = models.FloatField()
    imagen = models.ImageField(storage=BunnyStorage(), upload_to='comentarios/')
    status = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'        


    def __str__(self):
        return f'{self.user.username} - {str(self.puntuacion)}'