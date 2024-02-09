from django.db import models
from login.models import CustomUser

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
