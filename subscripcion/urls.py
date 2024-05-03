from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    # vistas view_init_page
    path("test", views.test, name="test"),
    path("checkout/<str:uid>/", views.renderCheckout, name="checkout"),
    path("createPaymentIntent/<str:uid>/", views.createPaymentIntent, name="createPaymentIntent"),
    path('success/<str:uid>/', views.successPayment, name='success'),
    path('failure', views.failurePayment, name='failure'),
    path('pending', views.pendingPayment, name='pending'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
