from django.shortcuts import render

# Create your views here.
def render_init_page(request):
    return render(request, 'login/init/inicio.html')


def render_detalle_lugar(request):
    return render(request, 'login/init/detalle.html')


def view_user_profile(request):


    return render(request, 'login/user/profile.html')


def view_user_login(request):
    return render(request, 'login/user/login.html')


def view_user_signup(request):
    return render(request, 'login/user/signup.html')

def view_user_recovery_password(request):
    return render(request, 'login/user/recovery_password.html')