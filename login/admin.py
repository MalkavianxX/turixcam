from django.contrib import admin
from .models import CustomUser, Favorito, Guardado, Idea, Comentario

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'horas', 'foto_perfil', 'foto_portada', 'fecha']

class FavoritoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'fecha', 'lugar']

class GuardadoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'fecha', 'lugar']

class IdeaAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'descripcion', 'imagen']

class ComentariosAdmin(admin.ModelAdmin):
    list_display= ['puntuacion', 'text','lugar','fecha','status']
# Registra tus modelos aquí
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Favorito, FavoritoAdmin)
admin.site.register(Guardado, GuardadoAdmin)
admin.site.register(Idea, IdeaAdmin)
admin.site.register(Comentario, ComentariosAdmin)
