from django.contrib import admin
from .models import CustomUser, Favorito, Guardado, Idea, Comentario, ImagenesDefault

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id','username', 'first_name', 'last_name', 'foto_perfil', 'foto_portada', 'premium','creditos']
    search_fields = ('username', 'email')
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ['id','usuario', 'fecha', 'camara']

class GuardadoAdmin(admin.ModelAdmin):
    list_display = ['id','usuario', 'fecha', 'camara']

class IdeaAdmin(admin.ModelAdmin):
    list_display = ['id','usuario', 'descripcion', 'imagen']

class ComentariosAdmin(admin.ModelAdmin):
    list_display= ['id','puntuacion', 'text','content_object','fecha','status']

class ImagenesDefaultAdmin(admin.ModelAdmin):
    list_display = ['id','tipo','imagen','acceso',]
# Registra tus modelos aquí
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Favorito, FavoritoAdmin)
admin.site.register(Guardado, GuardadoAdmin)
admin.site.register(Idea, IdeaAdmin)
admin.site.register(Comentario, ComentariosAdmin)
admin.site.register(ImagenesDefault, ImagenesDefaultAdmin)