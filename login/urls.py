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

    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)