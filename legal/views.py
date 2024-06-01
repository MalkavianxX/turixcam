from django.shortcuts import render

# Create your views here.
def view_tyc(request):
    return render(request, 'legal/tyc.html')

def view_aviso_privacidad(request):
    return render(request, 'legal/aviso_privacidad.html')