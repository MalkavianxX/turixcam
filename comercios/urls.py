from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    #vistas view_init_page
    path('comercio/<str:cm_id>/',views.view_detail_comercio, name='view_detail_comercio'),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)