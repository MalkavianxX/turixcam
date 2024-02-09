from django.db import models
from django_bunny.storage import BunnyStorage

class Stream(models.Model):
    url = models.URLField(max_length=2500)
    key = models.CharField(max_length=2500)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Stream'
        verbose_name_plural = 'Streams'

    def __str__(self): 
        return self.url

class Lugar(models.Model):
    titulo = models.CharField(max_length=250)
    pais = models.CharField(max_length=250)
    estado = models.CharField(max_length=250)
    municipio = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    cp = models.CharField(max_length=25)
    imagen_picture = models.ImageField(storage=BunnyStorage(), upload_to='Lugar-pictures/')
    imagen_fondo = models.ImageField(storage=BunnyStorage(), upload_to='Lugar-wallpaper/')
    descripcion = models.TextField(max_length=2500)
    puntuacion = models.FloatField(default=0.0)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, related_name='lugares')
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'

    def __str__(self):
        return self.titulo

class Etiqueta(models.Model):
    icono = models.URLField(max_length=2500)
    color = models.CharField(max_length = 250)
    titulo = models.CharField(max_length = 250)
    descripcion = models.TextField(max_length = 2500)

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'

    def __str__(self):
        return self.titulo

class Caracteristicas(models.Model):
    lugar = models.ForeignKey(Lugar, on_delete = models.CASCADE, related_name='caracteristicas')
    etiqueta = models.ForeignKey(Etiqueta, on_delete = models.CASCADE, related_name='caracteristicas')

    class Meta:
        verbose_name = 'Caracteristica'
        verbose_name_plural = 'Caracteristicas'
        unique_together = ('lugar', 'etiqueta',)

    def __str__(self):
        return f'{self.lugar.titulo} - {self.etiqueta.titulo}'

class Horas(models.Model):
    lugar = models.ForeignKey(Lugar, on_delete = models.CASCADE, related_name='horas')
    tiempo = models.FloatField(default = 0.0)

    class Meta:
        verbose_name = 'Hora'
        verbose_name_plural = 'Horas'

    def __str__(self):
        return f'{self.lugar.titulo} - {self.tiempo}'
