from django.http import JsonResponse
import json
from django.shortcuts import render, redirect
from django.contrib.auth import logout,authenticate, login
from login.models import CustomUser, Favorito, Guardado  # Importa tu modelo personalizado
from django.contrib.auth.hashers import make_password
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings

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
    return render(request, 'login/init/inicio.html')


def render_detalle_lugar(request):
    return render(request, 'login/init/detalle.html')

def get_user_profile(user):
    if user.custom_avatar_uploaded:
        avatar_url = user.foto_perfil.url
    elif user.socialaccount_set.exists():
        avatar_url = user.socialaccount_set.all().first().get_avatar_url
    else:
        avatar_url = 'https://turixcam-images.b-cdn.net/Backgrounds/fotodefault.jpg'
    if  user.foto_portada:
        portada = user.foto_portada.url
    else:
        portada = 'https://turixcam-images.b-cdn.net/Backgrounds/portada%20(1).jpg'

    context = {
        'avatar_url': avatar_url,
        'is_socialaccount': is_social_auth(user),
        'portada': portada
        
    }
    return context    

def get_favorites_profile(user):
    favoritos = Favorito.objects.filter(usuario=user).order_by('-fecha')
    return favoritos

def get_saved_profile(user):
    guardados = Guardado.objects.filter(usuario=user).order_by('-fecha')
    return guardados

@login_required
def view_user_profile(request):
    context = get_user_profile(request.user)
    context['favoritos'] = get_favorites_profile(request.user)
    context['guardados'] = get_saved_profile(request.user)


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
def function_update_wallpaper(request):
    if request.method == 'POST':
        try:
            user = request.user
            portada = request.FILES['image']
            if user.foto_portada:
                user.foto_portada.delete(save=False)  # Elimina la imagen anterior
            user.foto_portada = portada
            user.save()
            return JsonResponse({'message': 'Todo salió bien, la imagen se ha guardado correctamente.'}, status=200)
        except Exception as e:
            return JsonResponse({'message': f'Hubo un error al guardar la imagen: {str(e)}'}, status=500)
    else:
        return JsonResponse({'message': 'Fallo de método, se esperaba una solicitud POST.'}, status=405)

@login_required
def function_update_profile_picture(request):
    if request.method == 'POST':
        try:
            user = request.user
            foto_perfil = request.FILES['image']
            user.custom_avatar_uploaded = True 
            if user.foto_perfil:
                user.foto_perfil.delete(save=False)  # Elimina la imagen anterior
            user.foto_perfil = foto_perfil
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
    



def function_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'ok'}, status=200)
        else:
            return JsonResponse({'error': 'Usuario o contraseña incorrectos'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)


def function_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Ya existe un usuario con ese correo electrónico'}, status=400)
        
        user = CustomUser.objects.create_user(username=email, email=email, password=password,first_name = "Usuario001AAA ❤️", last_name = "Turixta especial")
        user.save()

        return JsonResponse({'status': 'ok'}, status=200)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
