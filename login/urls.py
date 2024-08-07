from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

 

urlpatterns = [
    #vistas render
    path('',views.render_init_page, name='render_init_page'),
    path('render_detalle_lugar',views.render_detalle_lugar, name='render_detalle_lugar'),
    path('profile',views.view_user_profile, name="view_user_profile"),
    path('login',views.view_user_login, name="view_user_login"),
    path('signup', views.view_user_signup, name="view_user_signup"),
    path('recovery_password',views.view_user_recovery_password, name="view_user_recovery_password"), 
    path('logout',views.function_logout, name="function_logout"),
    path('view_form', views.view_form, name="view_form"),

    #funciones
    path('up_images',views.function_update_profile_images, name="function_update_profile_images"),
    path('up_info',views.function_update_info_profile, name="function_update_info_profile"),
    path('up_password',views.function_update_password, name="function_update_password"),
    path('fun_login',views.function_login, name="function_login"),
    path('fun_signup',views.function_signup, name="function_signup"),
    path('fun_recovery',views.function_send_recovery_mail, name="function_send_recovery_mail"),
    path('send_email_init_page',views.send_email_init_page, name="send_email_init_page"),
    path('capturar_atencion',views.capturar_atencion, name="capturar_atencion"),


    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
