from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    #vistas render

    path('tycs',views.view_tyc, name="view_tyc"),
    path('aviso_privacidad',views.view_aviso_privacidad, name="view_aviso_privacidad"),

    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)