from django.contrib import admin
from .models import Personal  # Asegúrate de que la ruta de importación sea correcta

class PersonalAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','nombre','apellidop','telefono','correo']



admin.site.register(Personal,PersonalAdmin)
