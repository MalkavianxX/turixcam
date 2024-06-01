from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from login.models import (
    CustomUser,
    Favorito,
    Guardado,
    Comentario
)  # Importa tu modelo personalizado
from django.http import JsonResponse
from .models import Camara


def camara_existe_byID(id):
    return Camara.objects.filter(pk=id).exists()

# Create your views here.
def view_init_page(request):

    return render(request, "camaras/view_init_page.html")


def get_clase_favorito(usuario, camara, modelo):
    return "btn-danger" if modelo.objects.filter(usuario=usuario, camara=camara).exists() else "btn-outline-danger"

def get_clase_guardado(usuario, camara, modelo):
    return "btn-warning" if modelo.objects.filter(usuario=usuario, camara=camara).exists() else "btn-outline-warning"

def get_user_icon_profile(user):
    if user.custom_avatar_uploaded:
        avatar_url = user.foto_perfil.url
    elif user.socialaccount_set.exists():
        avatar_url = user.socialaccount_set.all().first().get_avatar_url
    else:
        avatar_url = user.foto_perfil.url  # Esto será la URL de la imagen predeterminada
  
    return avatar_url  

def get_all_coments(camara):
    comentarios = Comentario.objects.filter(camara=camara, status=True).order_by('-fecha')
    media = 0.0
    for iter in comentarios:
        iter.user.avatar_url = get_user_icon_profile(iter.user)
        media = media + iter.puntuacion
    if comentarios.count() > 0:
        media = media / comentarios.count()  
    return comentarios, "{0:.1f}".format(media)


def get_puntuaciones(camara):
    comentarios = Comentario.objects.filter(camara=camara)
    total_comentarios = comentarios.count()
    puntuaciones = {i: 0 for i in range(1, 6)}  # Inicializa un diccionario con las puntuaciones del 1 al 5

    for comentario in comentarios:
        puntuaciones[comentario.puntuacion] += 1

    # Calcula los porcentajes
    for puntuacion, count in puntuaciones.items():
        porcentaje = (count / total_comentarios) * 100 if total_comentarios > 0 else 0
        puntuaciones[puntuacion] = {
            'count': count,
            'percentage': round(porcentaje, 2)  # Redondea el porcentaje a dos decimales
        }

    # Ordena el diccionario por clave en orden descendente
    puntuaciones = {k: puntuaciones[k] for k in sorted(puntuaciones, reverse=True)}

    return puntuaciones



def view_detail_camara(request):
    camara = Camara.objects.get(pk=1)
    user = request.user   
    comentarios,media =  get_all_coments(camara)     
    if request.user.is_authenticated:
        context = {
            "camara": camara,
            "es_favorito": get_clase_favorito(user, camara, Favorito),
            "es_guardado": get_clase_guardado(user, camara, Guardado),
            "comentarios": comentarios,
            "total_comentarios": comentarios.count(),
            "media":media,
            "puntuaciones":get_puntuaciones(camara),
        }
    else:
        context = {
            "camara": camara,
            "es_favorito": "btn-outline-danger",
            "es_guardado": "btn-outline-warning",
            "comentarios": comentarios,
            "total_comentarios": comentarios.count(),
            "media":media,
            "puntuaciones":get_puntuaciones(camara),
        }           
    return render(request, "camaras/view_detail.html", context)



@login_required
def addFavorite(request):
    if request.method == "POST":
        user = request.user
        if request.user.is_authenticated:
            camara_id = request.POST.get("id_camara") 
            try:
                camara = Camara.objects.get(pk=camara_id)
            except Camara.DoesNotExist:
                return JsonResponse({"error": "El camara no existe."}, status=400)

            if Favorito.objects.filter(usuario=user, camara=camara).exists():
                Favorito.objects.get(usuario=user, camara=camara).delete()
                return JsonResponse({"message": "Camara eliminado.","add":"btn-outline-danger","del":"btn-danger",}, status=200)
            else:
                Favorito.objects.create(usuario=user, camara=camara)
                return JsonResponse({'message': 'Camara agregado.',"add":"btn-danger","del":"btn-outline-danger"}, status=200)
        else:
            return JsonResponse({"error": "El usuario no está autenticado."}, status=400)
    else:
        return JsonResponse({"error": "Fallo de método, se esperaba una solicitud POST."}, status=405)

@login_required
def addGuardado(request):
    if request.method == "POST":
        user = request.user
        if request.user.is_authenticated:
            camara_id = request.POST.get("id_camara")
            try:
                camara = Camara.objects.get(pk=camara_id)
            except Camara.DoesNotExist:
                return JsonResponse({"message": "El camara no existe."}, status=400)

            if Guardado.objects.filter(usuario=user, camara=camara).exists():
                Guardado.objects.get(usuario=user, camara=camara).delete()
                return JsonResponse({"message": "Camara eliminado.","add":"btn-outline-danger","del":"btn-danger",}, status=200)
            else:
                Guardado.objects.create(usuario=user, camara=camara)
                return JsonResponse({'message': 'Camara agregado.',"add":"btn-warning","del":"btn-outline-warning"}, status=200)
        else:
            return JsonResponse({"message": "El usuario no está autenticado."}, status=400)
    else:
        return JsonResponse({"message": "Fallo de método, se esperaba una solicitud POST."}, status=405)


@login_required
def addComentario(request):
    if request.method == "POST":
        user = request.user
        if user.is_authenticated:
            camara_id = request.POST.get("id_camara")
            text = request.POST.get("text")
            puntuacion = request.POST.get("puntuacion")
            if not text or not puntuacion:
                return JsonResponse({"message": "El comentario y la puntuación son obligatorios."}, status=400)
            try:
                camara = Camara.objects.get(pk=camara_id)
            except Camara.DoesNotExist:
                return JsonResponse({"message": "El camara no existe."}, status=400)
            Comentario.objects.create(user=user, camara=camara, text=text, puntuacion=float(puntuacion))
            return JsonResponse({'message': 'Comentario agregado.'}, status=200)
        else:
            return redirect('login')
            return JsonResponse({"message": "El usuario no está autenticado."}, status=400)
    else:
        return JsonResponse({"message": "Fallo de método, se esperaba una solicitud POST."}, status=405)