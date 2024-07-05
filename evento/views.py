from django.shortcuts import render
from camaras.models import Camara

def init_page_evento(request):
        
    camaras = Camara.objects.all().order_by('titulo')
    context = {
        'camaras' : camaras
    }
    return render(request, 'pages/init.html',context)