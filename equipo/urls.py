from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    #vistas view_init_page
    path('miembro/<str:id>/',views.miembro, name='miembro'),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)