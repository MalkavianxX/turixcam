from django.shortcuts import render

# Create your views here.
def render_init_page(request):
    return render(request, 'login/init/inicio.html')


def render_detalle_lugar(request):
    return render(request, 'login/init/detalle.html')
