from django.contrib import admin
from .models import Evento, Notificacion, EventoCultural, Imagen

class EventoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion', 'url_accion', 'fecha_inicio', 'fecha_cierre']

class NotificacionAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'evento', 'visto']
    
class ImagenInline(admin.TabularInline):
    model = Imagen
    extra = 1
    
class EventoCulturalAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'estado','fecha_inicio','fecha_cierre','cobertura',]
    inlines = [ImagenInline]
# Registra tus modelos aquí
admin.site.register(Evento, EventoAdmin)
admin.site.register(Notificacion, NotificacionAdmin)
admin.site.register(EventoCultural, EventoCulturalAdmin)
admin.site.register(Imagen)
 