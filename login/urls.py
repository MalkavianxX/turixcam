from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    #vistas render
    path('',views.render_init_page, name='render_init_page'),
    path('render_detalle_lugar',views.render_detalle_lugar, name='render_detalle_lugar'),

    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)