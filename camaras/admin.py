from django.contrib import admin
from .models import Stream, Camara

class StreamAdmin(admin.ModelAdmin):
    list_display = ['url', 'key', 'activo']
class CamaraAdmin(admin.ModelAdmin):
    list_display = ('titulo','estado','likes','stream',)

# Registra tus modelos aquí
admin.site.register(Stream, StreamAdmin)
admin.site.register(Camara, CamaraAdmin)