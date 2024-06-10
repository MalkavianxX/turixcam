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
    
    path('failure/<str:uid>/', views.failurePayment, name='failure'),
    path('pending', views.pendingPayment, name='pending'),

    path("createPaymentIntentFan/<str:uid>/", views.createPaymentIntentFan, name="createPaymentIntentFan"),
    path('successFAN/<str:uid>/', views.successPaymentFAN, name='successPaymentFAN'),



    path("createPaymentIntentsup/<str:uid>/", views.createPaymentIntentsup, name="createPaymentIntentsup"),
    path('successPaymentsup/<str:uid>/', views.successPaymentsup, name='successPaymentsup'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
