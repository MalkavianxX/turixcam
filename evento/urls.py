from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    #vistas render
    path('init_page_evento',views.init_page_evento, name='init_page_evento'),
    path('view_detail_evento/<str:id>/',views.view_detail_evento, name="view_detail_evento"),



    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)