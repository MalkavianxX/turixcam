from django.contrib import admin
from .models import Personal  # Asegúrate de que la ruta de importación sea correcta

class PersonalAdmin(admin.ModelAdmin):
    exclude = ('descripcion', 'foto_perfil', 'foto_portada',)

admin.site.register(Personal, PersonalAdmin)
