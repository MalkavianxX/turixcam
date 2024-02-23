
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('camaras/',include('camaras.urls')),
    path('evento/',include('evento.urls')),
    path('accounts/', include('allauth.urls')),
    path('equipo/', include('equipo.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)