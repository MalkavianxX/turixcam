
from django.contrib import admin
from .models import Comercio, Imagen

class ImagenInline(admin.TabularInline):
    model = Imagen
    extra = 1


class ComercioAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'estrellas', 'camara' ,'direccion',)
    inlines = [ImagenInline]

admin.site.register(Comercio, ComercioAdmin)
admin.site.register(Imagen)
