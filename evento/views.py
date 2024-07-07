from django.shortcuts import render
from camaras.models import Camara
from .models import EventoCultural
from camaras.views import get_all_coments, get_comercios, get_puntuaciones, get_clase_favorito, need_Adversiment, get_clase_guardado
import calendar
from django.utils import timezone

def calcular_diferencia(fecha_inicio):
    ahora = timezone.now()
    diferencia = fecha_inicio - ahora
    print(diferencia)
    
    if diferencia.days >= 30:
        # Calcula la diferencia en meses
        meses = diferencia.days // 30
        return meses, "mes" if meses == 1 else "meses"
    elif diferencia.days >= 1:
        # Calcula la diferencia en días
        return diferencia.days, "día" if diferencia.days == 1 else "días"
    else:
        # Calcula la diferencia en horas
        horas = abs(diferencia.total_seconds()) // 3600
        return horas, "hora" if horas == 1 else "horas"
 


def init_page_evento(request):
        
    camaras = Camara.objects.all().order_by('titulo')
    eventos = EventoCultural.objects.filter(fecha_inicio__gte=timezone.now()).order_by('fecha_inicio')
    estados_disponibles = []
    
    for item in eventos:
        item.mes = str(calendar.month_abbr[int(item.fecha_inicio.strftime('%m'))]).replace('.','').upper()
        item.dia = item.fecha_inicio.strftime('%d')[:2]
        item.fecha_corta = item.fecha_inicio.strftime("%d-%m ")
        print(item.cobertura)
        if item.estado not in estados_disponibles:
            estados_disponibles.append(item.estado)
    
    context = {
        'camaras' : camaras,
        'eventos':eventos, 
        'estados':estados_disponibles
    }
    return render(request, 'pages/init.html',context)

def view_detail_evento(request,id):

    camara = Camara.objects.get(pk=id)
    evento = EventoCultural.objects.get(pk = id)

    user = request.user   
    comentarios,media =  get_all_coments(evento)
    print(comentarios)     
    
    restaurantes = get_comercios(evento.municipio,'Restaurante') 
    atractivos = get_comercios(evento.municipio,'Atractivo')
    hoteles = get_comercios(evento.municipio,'Hotel')

    
    for lista in [hoteles, restaurantes, atractivos]:
        if lista: 
            for i in lista:  
                i.iconestrellas = i.set_estrellas()
                print(i.cliente)

    diferencia , determinador = calcular_diferencia(evento.fecha_inicio)
    context = {
        "evento": evento,
        "comentarios": comentarios,
        "total_comentarios": comentarios.count(),
        "media":media,
        "puntuaciones":get_puntuaciones(evento),
        "hoteles": hoteles,
        "atractivos": atractivos,
        "restaurantes": restaurantes,
        "need_ad": str( need_Adversiment(request, evento.id)),
        "time": 12,
        "diferencia":diferencia,
        "determinador":determinador,
    }


    

    camara.register_view()
    return render(request, "pages/view.html", context)