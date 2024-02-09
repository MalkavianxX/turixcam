from django.contrib import admin
from .models import Stream, Lugar, Etiqueta, Caracteristicas, Horas

class StreamAdmin(admin.ModelAdmin):
    list_display = ['url', 'key', 'activo']

class LugarAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'pais', 'estado', 'municipio', 'direccion', 'cp', 'imagen_picture', 'imagen_fondo', 'descripcion', 'puntuacion', 'stream', 'activo']

class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ['icono', 'color', 'titulo', 'descripcion']

class CaracteristicasAdmin(admin.ModelAdmin):
    list_display = ['lugar', 'etiqueta']

class HorasAdmin(admin.ModelAdmin):
    list_display = ['lugar', 'tiempo']

# Registra tus modelos aquí
admin.site.register(Stream, StreamAdmin)
admin.site.register(Lugar, LugarAdmin)
admin.site.register(Etiqueta, EtiquetaAdmin)
admin.site.register(Caracteristicas, CaracteristicasAdmin)
admin.site.register(Horas, HorasAdmin)
