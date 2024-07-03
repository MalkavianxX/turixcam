
from pathlib import Path
import os
import firebase_admin
from firebase_admin import credentials ,firestore
import stripe
import json

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-7@-@+wzqd+*@34%3)6=%*p(er_c(sn$arx+e%pj$jzr*fkfrye'

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
    'firebase_admin',



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



# Obtener el contenido del JSON desde la variable de entorno
firebase_credentials = os.environ.get('FIREBASE_CREDENTIALS')
json_data = json.loads(firebase_credentials)


# Inicializar la aplicación de Firebase con las credenciales
cred = credentials.Certificate(json_data)
firebase_admin.initialize_app(cred)

# Obtener una referencia a la base de datos Firestore
DB = firestore.client()



stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
STRIPE_PMC = os.environ.get('STRIPE_PMC')
STRIPE_PRICE = os.environ.get('STRIPE_PRICE')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'