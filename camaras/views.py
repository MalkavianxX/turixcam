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
from comercios.models import Comercio
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from comercios.models import Comercio
from evento.models import EventoCultural
def camara_existe_byID(id):
    return Camara.objects.filter(pk=id).exists()

@login_required
def view_init_page(request,id):
    comercios = []
    class comerciotemp():
        def __init__(self,id,camara,titulo,portada) -> None:
            self.id = id
            self.camara = camara
            self.cliente = titulo
            self.portada = portada
    if id == 'None':
        estados = []
        camaras = Camara.objects.all().order_by('titulo')



            
        municipios = []
        estados = []
        for i in camaras:
            if i.municipio not in municipios:
                municipios.append(i.titulo)
            if i.estado not in estados:
                com = Comercio.objects.filter(camara = i.titulo)[:4]
                for i in com:
                    comercios.append(comerciotemp(
                        i.id,i.camara,i.cliente,i.portada.url
                    ))
                estados.append(i.estado)
            

        context = {
            'camaras':camaras,
            'municipios':municipios,
            'estados': estados, 
            'comercios': comercios,
        }        

        return render(request, "camaras/view_init_page.html",context)
    else:
                
        estados = []
        camaras = Camara.objects.all().order_by('titulo')
        cam_cuestion = Camara.objects.get(pk = id)
        lugares = Camara.objects.filter(estado = cam_cuestion.estado).order_by('titulo')
            
        municipios = []
        estados = []
        for i in camaras:
            if i.municipio not in municipios:
                municipios.append(i.municipio)
            if i.estado not in estados:

                estados.append(i.estado)
        for i in lugares:
            com = Comercio.objects.filter(camara = i.titulo)[:5]
            for i in com:
                comercios.append(comerciotemp(
                    i.id,i.camara,i.cliente,i.portada.url
                ))

        context = {
            'camaras':lugares,
            'municipios':municipios,
            'estados': estados, 
            'comercios': comercios,
        }        

        return render(request, "camaras/view_init_page.html",context)



def get_clase_favorito(usuario, camara, modelo):
    return "btn-danger" if modelo.objects.filter(usuario=usuario, camara=camara).exists() else "btn-outline-danger"

def get_clase_guardado(usuario, camara, modelo):
    return "btn-warning" if modelo.objects.filter(usuario=usuario, camara=camara).exists() else "btn-outline-warning"

def get_user_icon_profile(user):
    avatar_url = user.foto_perfil
  
    return avatar_url  

 
def get_all_coments(obj):
    obj_content_type = ContentType.objects.get_for_model(obj)
    comentarios = Comentario.objects.filter(content_type=obj_content_type, object_id=obj.id, status=True).order_by('-fecha')
    media = 0.0
    for iter in comentarios:
        iter.user.avatar_url = get_user_icon_profile(iter.user)
        media = media + iter.puntuacion
    if comentarios.count() > 0:
        media = media / comentarios.count()  
    return comentarios, "{0:.1f}".format(media)


def get_puntuaciones(obj):
    obj_content_type = ContentType.objects.get_for_model(obj)
    comentarios = Comentario.objects.filter(content_type=obj_content_type, object_id=obj.id)
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


from django.core.cache import cache

def need_Adversiment(request, camara_id):
    # Obtener las cámaras visitadas de la caché o establecer una lista vacía
    camaras_visitadas = cache.get('camaras_visitadas', [])
    print(camaras_visitadas)
    # Verificar si el ID de la cámara ya está en la lista
    if camara_id not in camaras_visitadas:
        # Agregar el ID de la cámara actual si aún no está en la lista
        camaras_visitadas.append(camara_id)
        cache.set('camaras_visitadas', camaras_visitadas, 3600)  # Almacena en caché durante 1 hora
        print("se agrego")
        print(camaras_visitadas)
        return "true"
    else:
        return "false"



def view_detail_camara(request,id):

    camara = Camara.objects.get(pk=id)
    camaras = Camara.objects.all().order_by('titulo')


    user = request.user   
    comentarios,media =  get_all_coments(camara)     
    restaurantes = get_comercios(camara.titulo,'Restaurante') 
    atractivos = get_comercios(camara.titulo,'Atractivo')
    hoteles = get_comercios(camara.titulo,'Hotel')

    
    for lista in [hoteles, restaurantes, atractivos]:
        if lista: 
            for i in lista:  
                i.iconestrellas = i.set_estrellas()
                print(i.cliente)

   
    context = {
        "camara": camara,
        "comentarios": comentarios,
        "total_comentarios": comentarios.count(),
        "media":media,
        "puntuaciones":get_puntuaciones(camara),
        "hoteles": hoteles,
        "atractivos": atractivos,
        "restaurantes": restaurantes,
        "need_ad": str( need_Adversiment(request, camara.id)),
        "time": 12,
    }

    if request.user.is_authenticated:
        context["es_favorito"] = get_clase_favorito(user, camara, Favorito)
        context["es_guardado"] = get_clase_guardado(user, camara, Guardado)
    else:
        context["es_favorito"] = "btn-outline-danger"
        context["es_guardado"] = "btn-outline-warning"
        
    if request.user.premium != 'free':
        camaras_js = [{'lat': c.latitude, 'lng': c.longitude, 'icon': c.pin.url, 'id': c.id } for c in camaras]
        print("locaionew: ",camaras_js)
        context['locaciones'] = camaras_js

    camara.register_view()
    return render(request, "camaras/view_detail.html", context)




def get_comercios(camara_name,type):
    comercios = Comercio.objects.filter(camara=camara_name, tipo=type)
    if not comercios.exists():
        comercios = False
    return comercios 


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
        object_id = request.POST.get("object_id")
        object_type = request.POST.get("object_type")
        text = request.POST.get("text")
        puntuacion = request.POST.get("puntuacion")
        app_label = request.POST.get("app_label")
        print(app_label)
        print(object_id)
        print(object_type)
        if not text or not puntuacion:
            return JsonResponse({"message": "El comentario y la puntuación son obligatorios."}, status=400)

        try:
            content_type = ContentType.objects.get(app_label=app_label, model=object_type)
            model_class = content_type.model_class()
            obj = model_class.objects.get(pk=object_id)
        except ContentType.DoesNotExist:
            
            return JsonResponse({"message": "El tipo de objeto no existe."}, status=400)
        except ObjectDoesNotExist:
            return JsonResponse({"message": "El objeto no existe."}, status=400)

        comentario = Comentario.objects.create(user=user, content_object=obj, text=text, puntuacion=float(puntuacion))

        return JsonResponse({
            'message': 'Comentario agregado.',
            'comentario': {
                'username': comentario.user.username,
                'puntuacion': comentario.puntuacion,
                'text': comentario.text,
                'fecha': comentario.fecha.strftime('%d-%m-%Y'),
                'avatar_url': comentario.user.foto_perfil,
            }
        }, status=200)
    else:
        return JsonResponse({"message": "Fallo de método, se esperaba una solicitud POST."}, status=405)



@login_required
def remove_comentario(request,id):
    try:
        comentario = Comentario.objects.get(pk = id)
        id_camara = comentario.object_id
        comentario.delete()
        return redirect('view_detail_camara',id = id_camara)
    except Exception as e:
        print(e)
    pass