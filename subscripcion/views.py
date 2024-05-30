from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
import stripe
from django.conf import settings
from .FireUser import FireUser
from .UsuarioInfo import User  

from django.http import FileResponse
from django.views import View
import os

class AppleMerchantIdView(View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static/.well-known/apple-developer-merchantid-domain-association')
        return FileResponse(open(file_path, 'rb')) 


stripe.api_key = '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'

def renderCheckout(request,uid):
    user = FireUser.get(uid = uid)
    if user is not None:

        if not user.photo_url :
            foto = 'https://turixcam-images.b-cdn.net/Recursos%20WEB/Fotos%20Perfil%20Defecto/D.png'
        else:
            foto = user.photo_url
        context = {
            'email': user.email,
            'usuario': user.display_name,
            'foto':foto,
            'uid': uid,
        }
        return render(request,"pagos/checkout/checkout.html",context)
    else:
        print(user)
    return render(request,"pagos/checkout/checkout.html",context)


def successPayment(request,uid):
    try:
        print(uid)
        email = FireUser.get(uid = uid)
        print(email.email)
        user = User.get(correo = email.email)
        user.premium = 'Mega fan'
        user.creditos = int(user.creditos) + 15
        user.save()
    except Exception as e:
        print(e)
    return render(request,"pagos/estados/success.html")


def successPaymentFAN(request,uid):
    try:
        print(uid)
        email = FireUser.get(uid = uid)
        print(email.email)
        user = User.get(correo = email.email)
        user.premium = 'Fan'
        user.creditos = int(user.creditos) + 5
        user.save()
    except Exception as e:
        print(e)
    return render(request,"pagos/estados/success.html")


def createPaymentIntentFan(request,uid):

  session = stripe.checkout.Session.create(
    line_items=[{
        'price': "price_1PLy8PKusDeFdtimmD8TtOEX",
        'quantity': 1,
    }],
    mode='payment',
    payment_method_configuration='pmc_1PLWr5KusDeFdtimWP2dHKoE',

    success_url='https://turixcam.com/subscripcion/successFAN/'+uid+'/',
    cancel_url='https://turixcam.com/subscripcion/failure',
  )

  return redirect(session.url, code=303)

def failurePayment(request):
    return render(request,"pagos/estados/failure.html")


def pendingPayment(request):
    return render(request,"pagos/estados/pending.html")

def createPaymentIntent(request,uid):

  session = stripe.checkout.Session.create(
    line_items=[{
        'price': "price_1PLWjZKusDeFdtimHAcVHkk7",
        'quantity': 1,
    }],
    mode='payment',
    payment_method_configuration='pmc_1PLWr5KusDeFdtimWP2dHKoE',

    success_url='https://turixcam.com/subscripcion/success/'+uid+'/',
    cancel_url='https://turixcam.com/subscripcion/failure',
  )

  return redirect(session.url, code=303)
@require_http_methods(["GET"])
def test(request):
    try:
        starter_subscription = stripe.Product.create(
        name="Starter Subscription",
        description="$12/Month subscription",
        )

        starter_subscription_price = stripe.Price.create(
        unit_amount=1200,
        currency="usd",
        recurring={"interval": "month"},
        product=starter_subscription['id'],
        )

        # Save these identifiers
        solve = "Success! Here is your starter subscription product id: {starter_subscription.id}"
        dos = "Success! Here is your starter subscription price id: {starter_subscription_price.id}"

    
        return JsonResponse({'status': 'OK', 'message': 'Operation successful', "solve":solve,"dos":dos}, safe=False,status=200)
    except Exception as e:
        return JsonResponse({'status': 'BadRequest', 'message': str(e)}, status=400)        
    


from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .FireUser import FireUser

@require_http_methods(["GET"])
def createUserApi(request):
    try:
        users = FireUser.all()
        for i in users:
            print(i.uid)
            print(i.email)
            print(i.display_name)
            
        
        if users is not None:
            return JsonResponse({'status': 'OK', 'message': 'Usuarios citado'}, safe=False, status=200)
        else:
            return JsonResponse({'status': 'BadRequest', 'message': 'No se pudo crear el usuario'}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'BadRequest', 'message': str(e)}, status=400)

