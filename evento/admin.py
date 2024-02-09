from django.contrib import admin
from .models import Evento, Notificacion

class EventoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion', 'url_accion', 'fecha_inicio', 'fecha_cierre']

class NotificacionAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'evento', 'visto']

# Registra tus modelos aquí
admin.site.register(Evento, EventoAdmin)
admin.site.register(Notificacion, NotificacionAdmin)
