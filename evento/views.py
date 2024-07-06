from django.shortcuts import render
from camaras.models import Camara
from .models import EventoCultural
import calendar
import locale
import datetime

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

def init_page_evento(request):
        
    camaras = Camara.objects.all().order_by('titulo')
    eventos = EventoCultural.objects.all().order_by('fecha_inicio')
    estados_disponibles = []
    for item in eventos:
        item.mes = str(calendar.month_abbr[int(item.fecha_inicio.strftime('%m'))]).replace('.','').upper()
        item.dia = item.fecha_inicio.strftime('%d')[:2]
        print(item.cobertura)
        if item.estado not in estados_disponibles:
            estados_disponibles.append(item.estado)
    
    context = {
        'camaras' : camaras,
        'eventos':eventos, 
        'estados':estados_disponibles
    }
    return render(request, 'pages/init.html',context)