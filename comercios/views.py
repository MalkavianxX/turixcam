from django.shortcuts import render
from django.http import JsonResponse
from .models import Comercio, Imagen
from camaras.models import Camara
from camaras.views import get_all_coments, get_puntuaciones
# Create your views here.
def nada(request):
    return JsonResponse({'status': 'success', 'message': 'Correo enviado correctamente.'})

def view_detail_comercio(request,cm_id):
    try:
 
        comercio = Comercio.objects.get(pk = cm_id)
        comercio.iconestrellas = comercio.set_estrellas()
        imagenes = Imagen.objects.filter(comercio = comercio)
        comentarios,media =  get_all_coments(comercio)   
        context = {
            'comercio':comercio,
            'images':imagenes,
            "total_comentarios": comentarios.count(),
            "puntuaciones":get_puntuaciones(comercio),
            "comentarios": comentarios,
            "media":media,
        }

        
        return render(request, 'cliente/index.html',context)
    except Exception as e:
        print(e)
        return render(request, 'cliente/index.html') 