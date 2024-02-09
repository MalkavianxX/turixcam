from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    #vistas view_init_page
    path('buscar',views.view_init_page, name='view_init_page'),
    path('detalle',views.view_detail_camara, name="view_detail_camara"),


    #funciones jsonresponse
    path('addFavorite',views.addFavorite, name='addFavorite'),
    path('addGuardado',views.addGuardado, name='addGuardado'),
    path('addComentario',views.addComentario, name='addComentario'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)