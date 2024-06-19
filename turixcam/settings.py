
from pathlib import Path
import os
import firebase_admin
from firebase_admin import credentials ,firestore
import stripe
import json

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = True


if not DEBUG:
    SECURE_SSL_REDIRECT = True

if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',
    'camaras',
    'evento',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_bunny',
    'equipo',
    'subscripcion',
    'legal',
    'comercios',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",

]

ROOT_URLCONF = 'turixcam.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'turixcam.wsgi.application'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


CSRF_TRUSTED_ORIGINS = ['https://turixcam.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'turixdata',
        'USER': 'root',
        'PASSWORD': 'Rmpv54321',
        'HOST': 'postgresql-174165-0.cloudclusters.net',  
        'PORT': '10004',        
    }
}



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]




LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True




STATIC_URL = 'static/'
STATIC_ROOT =  os.path.join(BASE_DIR,'static') 
MEDIA_URL= '/media/'
MEDIA_ROOT =  os.path.join(BASE_DIR,'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'login.CustomUser'


LOGIN_REDIRECT_URL = "/login"
LOGUT_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = 'render_init_page'
LOGIN_URL = 'view_user_login'
 
SOCIALACCOUNT_LOGIN_ON_GET = True
ACCOUNT_ADAPTER = 'login.myadapter.MyAccountAdapter'
SOCIALACCOUNT_AUTO_SIGNUP = True
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}
 


BUNNY_USERNAME = os.environ.get('BUNNY_USERNAME')
BUNNY_PASSWORD = os.environ.get('BUNNY_PASSWORD')
BUNNY_REGION = os.environ.get('BUNNY_REGION')
BUNNY_HOSTNAME =  os.environ.get('BUNNY_HOSTNAME')



EMAIL_HOST = os.environ.get('EMAIL_HOST')  
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD =  os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True  


json__string = '{"type": "service_account", "project_id": "turixcamapp", "private_key_id": "ccc6dd63f9dc808571eb4397ab15bfeb6b618f95", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC7JcAI3jE2WW4m\nok7GHO60UWlUD57/pLHEAmpFO4S322N49BrqR739eok4jbN65D3FgX0UJ5tAtmwV\nYS6xUa2eWQyQmhllFnsdAornlIJMKeJKs7SP0vNf0UX0Q7iPvARp4ZcKbjsKmH+j\nouvk8zfXSQVNuSfHlSEYWfwS5Ez+AFFSeJ+XQsHSD3dkdPdlsUD4OPYxZBBdK53Q\neCdhGNkl2sB+B9d1tKndS6dnGse8zVe6y3Bl+elmLFwmxFjdvgniQQtG2XAZyIzN\nHZzLj1YtxkOm7kR011mh5bGlZEVv5zD350R+xR8PYlAxB5BK/h0YmwNtorBD4UAU\nVzrdHJX3AgMBAAECggEACnULi/NOcKkCnKoJGMzZEb5S0l2lFsfPHxK7eW7f9Z4O\nqt2I+3pSxW0pab2RP9atFPItWQj1heIrm+44O7RCrUxwhUv3C0z8SByyQkpsFXFp\nsZ7lAfxZmQsKi6GVGIL7BCeU1wJdzjPDPhOGdt6YSjFMWJF2BZLxrHiquyuCmda2\nPhif3B3U31oIP61ShwtfCZJufcAagb4Lkwox+6n7D9VSYrmfE4oicoabed420oSs\n0y/jnh/ymfrxo5b1StBA+bUsEK+eO/N/QeZ8YT/2KIdOT53ae/0qUwly716YILcd\nT2AXXQmBpFTmncpI+kl8J3tzNjSGyTrWMxQCTiCk4QKBgQDdStJ4vVzjNsfWAYQK\nHnhD5UJuxg5dUKnufYEhWBfrAQiNREEh0QcwQpNRZK/OyC1Ga+NLcYqDjyndMDIA\nBjM0RoQBi5r6ZO0NcqQJ9qDWogFSQ7I+GKGMbDws5FFyQzOM/25nd/NH1fwhaUaa\n6NDiSYN/IPGtdW8pqQLCqolDOQKBgQDYf/fyOqvHCPiGANJLEWazvtT4GM2Ali9h\nyoWz1Y3zv9ks7kanTRG5CK4hIFwamYBgLFKgaO5MZhJSUzoQA8FgclfUDXoYnskY\n6WIQruDWeekYnGgy+NOhSzWdTeZCYBEI4d0yyzKvP6chT0+D9EAS5O45GoQzepVc\nVRW8atqyrwKBgGXiszEADqpWaH+xxvdZvAmWnpWd/rMcFoFFq5SMmMaMfUF9cXd+\nZA7mOCm7b+6G38GSnt33cszLt3ytWfgE4sJozRJhEoPCwBn29GvZ74eio3Ua0hAh\nCxA6LSKGJLG1GyEJ4e0lnw8uCJ3heK6ODs6BBlgb9OnmLb5CoJC8L+KRAoGBAL4N\nYGCw5ni7xEcGU5T4eprRq+z7APOfY4rKGSLsFkfio0hRB474FdXD6/BCkvf6xnom\njoYodwB0HiNM0kyar1f2KGmLRyJzyX7n6WFR0ygULu6e5s3QJx+RgUhMyRR9dpbA\nh8h+Hkk/bHzOPbRNZy3u770LLQBv3MwIGSOk/cUbAoGBAKPaxypg/IMePeZIcwsr\nj4E+AH4cBDss0xkAF5qPWJLLGPiKWnUGAIA7z7/bNN9/NoZ6F7IKrvxpx4xvxeL3\niXNELCFzpqZGy41R9BYIYz8P6+yfbvlQYivg7tRjhmxtFmjl51bLs4aOFADBjWfM\nT1AZhfdGA+0kgHQrDtLHifVl\n-----END PRIVATE KEY-----\n", "client_email": "firebase-adminsdk-idm6c@turixcamapp.iam.gserviceaccount.com", "client_id": "110443898968448359497", "auth_uri": "https://accounts.google.com/o/oauth2/auth", "token_uri": "https://oauth2.googleapis.com/token", "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs", "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-idm6c%40turixcamapp.iam.gserviceaccount.com", "universe_domain": "googleapis.com"}'
config_json = json.loads(json__string)
cred = credentials.Certificate(config_json)
firebase_admin.initialize_app(cred)
DB= firestore.client()



stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'