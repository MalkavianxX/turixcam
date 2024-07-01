# Importaciones de Django
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


# Importaciones de modelos
from login.models import CustomUser, Favorito, Guardado, ImagenesDefault
from allauth.socialaccount.models import SocialAccount
from camaras.models import Camara 
from comercios.models import Comercio
# Otras importaciones
from subscripcion.FireUser import FireUser
import requests
import json

def maintenance_view(request):
    return render(request, 'login/init/maintenance.html') 

def function_send_recovery_mail(request):
    try:
        data = json.loads(request.body)
        email = data.get('email')
        subject = 'Reestablece tu contraseña'
        template = get_template('login/email/recovery_password.html')
        content = template.render()
        message = EmailMultiAlternatives(subject, '', settings.EMAIL_HOST_USER, [email])
        message.attach_alternative(content, 'text/html')
        message.send()
        return JsonResponse({'status': 'success', 'message': 'Correo enviado correctamente.'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})


# Llama a la función para enviar el correo de prueba


def is_social_auth(user):
    social_accounts = SocialAccount.objects.filter(user=user)
    if social_accounts.exists():
        # El usuario inició sesión a través de un proveedor externo
        provider = social_accounts.first().provider  # Esto será 'google', 'facebook', etc.
        return True, provider
    else:
        # El usuario inició sesión directamente en tu aplicación
        return False, None
# Create your views here.

def render_init_page(request):
    camaras = Camara.objects.all()
    comercios = Comercio.objects.filter(estrellas = 5).order_by('importancia')[:5]
    estados = []
    
    filter_camaras = []
    for cam in camaras:
        if cam.estado not in estados:
            estados.append(cam.estado)
            filter_camaras.append(cam)
            
    context = {
        'camaras':filter_camaras,
        'estados':estados,
        'comercios':comercios,
    } 
    
    return render(request, 'login/init/inicio.html', context)


def render_detalle_lugar(request):
    return render(request, 'login/init/detalle.html')



def get_favorites_profile(user):
    favoritos = Favorito.objects.filter(usuario=user).order_by('-fecha')
    return favoritos 
 
def get_saved_profile(user):
    guardados = Guardado.objects.filter(usuario=user).order_by('-fecha')
    return guardados

@login_required
def view_user_profile(request):
    context = {}
    context['favoritos'] = get_favorites_profile(request.user)
    context['guardados'] = get_saved_profile(request.user)
    print(request.user.premium)
    if request.user.premium == "free":

        context['portadas'] = ImagenesDefault.objects.filter(tipo = 'Portada',acceso = 'free')
        context['perfiles'] = ImagenesDefault.objects.filter(tipo = 'Perfil', acceso = 'free')
    else:
        context['portadas'] = ImagenesDefault.objects.filter(tipo = 'Portada')
        context['perfiles'] = ImagenesDefault.objects.filter(tipo = 'Perfil')

    return render(request, 'login/user/profile.html',context)

 
def view_user_login(request):
    
    return render(request, 'login/user/login.html')


def view_user_signup(request):
    return render(request, 'login/user/signup.html')

def view_user_recovery_password(request):
    return render(request, 'login/user/recovery_password.html')



@login_required
def function_logout(request):
    logout(request)
    return redirect('/')
 
@login_required()
def function_update_profile_images(request):
    if request.method == 'POST': 
        try:
            user = request.user
            portada_id = request.POST.get('portada')  
            perfil_id = request.POST.get('perfil') 

            if portada_id:
                portada = ImagenesDefault.objects.filter(pk = portada_id)
                if portada.exists() and user.foto_portada != portada[0].imagen.url:
                    user.foto_portada = portada[0].imagen.url
                    user.save()

            if perfil_id:
                perfil = ImagenesDefault.objects.filter(pk = perfil_id)
                if perfil.exists() and user.foto_perfil != perfil[0].imagen.url:
                    user.foto_perfil = perfil[0].imagen.url
                    user.save()

            

            return JsonResponse({'message': 'Todo salió bien, la imagen se ha guardado correctamente.'}, status=200)
        except Exception as e:
            return JsonResponse({'message': f'Hubo un error al guardar la imagen: {str(e)}'}, status=500)
    else:
        return JsonResponse({'message': 'Fallo de método, se esperaba una solicitud POST.'}, status=405)




@login_required
def function_update_info_profile(request):
    if request.method == 'POST':
        user = request.user
        up_username = request.POST.get('username')
        up_name = request.POST.get('name')
        up_last_name = request.POST.get('lastname')           
        up_email = request.POST.get('email')
        print(up_email, up_last_name, up_username, up_name)
        # Verificar si el correo electrónico ya está en uso
        if CustomUser.objects.filter(email=up_email).exclude(username=user.username).exists():
            return JsonResponse({'error': 'Este correo electrónico ya está en uso'}, status=400)

        user.username = up_username
        user.first_name = up_name
        user.last_name = up_last_name
        user.email = up_email
        user.save()
        
        return JsonResponse({'message': 'Formulario enviado exitosamente'})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    

@login_required
def function_update_password(request):
    if request.method == 'POST':
        user = request.user
        new_password = request.POST.get('new_password')

        # Validar la nueva contraseña
        if not new_password or len(new_password) < 7:
            return JsonResponse({'error': 'La contraseña debe tener al menos 8 caracteres'}, status=400)

        # Actualizar la contraseña del usuario
        user.password = make_password(new_password)
        user.save()

        return JsonResponse({'message': 'Contraseña actualizada exitosamente'})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)    
    

def get_user_by_email(correo):
    # Define la URL de tu API
    url = 'http://192.168.1.93:5000/api/getUserbyFirebase'

    # Define los datos que quieres enviar
    data = {
        'correo': correo,
    }

    # Convierte los datos a JSON
    data_json = json.dumps(data)

    # Define los encabezados de la solicitud
    headers = {
        'Content-Type': 'application/json',
    }

    # Realiza la solicitud POST
    response = requests.post(url, data=data_json, headers=headers)

    # Decodifica la respuesta JSON
    data = response.json()

    # Verifica si la API retornó un error
    if data.get('error'):
        return None

    # Retorna el diccionario del usuario
    return data.get('user')

def get_user_by_id(user_id):
    # Obtén una referencia al documento que quieres
    doc_ref = settings.DB.collection('Usuarios').document(user_id)

    # Obtén el documento
    doc = doc_ref.get()

    if doc.exists:
        # Si el documento existe, devuelve sus datos
        return doc.to_dict()
    else:
        # Si el documento no existe, devuelve None
        return None

def function_login(request):
    # Solo se permite el método POST para esta vista
    if request.method != 'POST':
        return JsonResponse({'message': 'Método no permitido'}, status=405)

    # Extraer las credenciales del usuario del cuerpo de la solicitud
    email = request.POST['username']
    password = request.POST['password']

    try:
        # Verificar si el usuario tiene cuenta en turixcam.com
        user_exists = CustomUser.objects.filter(email=email).exists()

        if user_exists:
            # Autenticar al usuario en turixcam.com
            print("existe el usuario en turixcam.com")
            user = authenticate(request, username=email, password=password)

            if user is not None:
                # Iniciar sesión y devolver un mensaje de éxito
                login(request, user)
                return JsonResponse({'message': 'Usuario creado e inició sesión exitosamente.','status':'200'}, status=200)
            else:
                # Las credenciales son inválidas
                print("existe en turixcam.com pero no son las credenciales correctas")
                return JsonResponse({'message': 'Error, correo o contraseña invalidos.'}, status=400)
        else:
            # Verificar si el usuario tiene cuenta en appturixcam
            firebase_user = FireUser.get_by_email(email)
            print("Se encontró un usuario en la app")
            if firebase_user is not None :

                # Obtén los detalles del usuario de Firebase
                user_details = get_user_by_id(email)
                print(user_details)
                if user_details is not None:
                    # Crea un nuevo usuario en Django
                    print("rellenando informacion del usariop app a web")
                    new_user = CustomUser(
                        foto_portada=user_details.get('portada'),
                        foto_perfil=user_details.get('image'),
                        premium=user_details.get('premium'),
                        creditos=int(user_details.get('creditos')),
                        email=user_details.get('correo'),
                        username=user_details.get('nombre'),
                    )
                    new_user.save()
                    new_user.set_password(password)
                    new_user.save()
                    # Sincroniza los favoritos del usuario
                    print("se creo el usuairo en web")
                    print("sincronizando faovritos")
                    favs_list = user_details.get('f1')  # No necesitas usar json.loads aquí
                    for fav in favs_list:
                        camara = Camara.objects.get(createdAt=int(fav))
                        new_fav = Favorito(usuario=new_user, camara=camara)
                        new_fav.save()
                    print("favoritos sincroniuzados")
                    # Iniciar sesión y devolver un mensaje de éxito
                    user = authenticate(request, username=new_user.username, password=password)
                    if user is not None:
                        # Aquí especificamos el backend de autenticación
                        backend = 'django.contrib.auth.backends.ModelBackend'
                        user.backend = backend
                        login(request, user)
                        return JsonResponse({'message': 'Usuario creado e inició sesión exitosamente.','status':'200'}, status=200)
                    else:
                        return JsonResponse({'message': 'Error en la contraseña o correo.'}, status=400)

                else:
                    # El usuario no existe en Firebase
                    return JsonResponse({'message': 'Error, No se encontró una cuenta asociada a ese correo.'}, status=400)
            else:
                # El usuario no existe en Django ni en Firebase
                return JsonResponse({'message': 'Error, No se encontró una cuenta asociada a ese correo.'}, status=400)

        

    except Exception as e:
        # Devolver un mensaje de error si ocurre alguna excepción
        return JsonResponse({'message': f'Hubo un error al crear el usuario: {str(e)}'}, status=500)




def create_user_document(user_id, user_data):
    # Obtén una referencia a la colección de usuarios
    users_ref = settings.DB.collection('Usuarios')

    # Crea un nuevo documento en la colección de usuarios
    users_ref.document(user_id).set(user_data)


@csrf_exempt  
def function_signup(request):
    # Solo se permite el método POST para esta vista
    if request.method != 'POST':
        return JsonResponse({'error': True, 'message': 'Método no permitido'}, status=405)

    try:
        # Extraer las credenciales del usuario
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Verificar que los campos requeridos estén presentes
        if not all([email, password]):
            return JsonResponse({'error': True, 'message': 'Faltan campos requeridos'}, status=400)

        # Verificar si el usuario ya existe en turixcam.com
        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({'error': True, 'message': 'Ya existe un usuario con ese correo electrónico'}, status=400)

        # Crear un nuevo usuario en turixcam.com
        user = CustomUser.objects.create_user(username=email, email=email, first_name="Turixta")
        user.save()
        user.set_password(password)
        user.save()
        # Verificar si el usuario existe en Firebase
        firebase_user = FireUser.get_by_email(email)
        if firebase_user is None:
            # Crear el usuario en Firebase
            firebase_user = FireUser(email=user.email, password=password)
            firebase_user.save()
            user_data = {
                'correo':user.email,
                'creditos':0,
                'f1': [],
                'image':user.foto_perfil,
                'nombre': 'Turixta',
                'portada':user.foto_portada,
                'premium':'free',
            }
            create_user_document(user.email,user_data)

        # Autenticar al usuario en Django
        django_user = authenticate(request, username=email, password=password)
        if django_user is not None:
            backend = 'django.contrib.auth.backends.ModelBackend'
            django_user.backend = backend
            login(request, django_user)
            return JsonResponse({'message': 'Usuario creado e inició sesión exitosamente.','status':'200'}, status=200)



    except Exception as e:
        # Manejo de errores generales
        return JsonResponse({'error': True, 'message': 'Error al crear el usuario: {}'.format(str(e))}, status=500)

