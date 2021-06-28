import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#BASE_DIR = '/home2/dtechnol/dtech'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a#)d3hat2$ghq1*qj7akhcs^@e9%qq+@^!^9v$*1-=w3^#99io'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'http://www.dtechnologies.co.ke',
    'dtechnologies.co.ke',
    'www.dtechnologies.co.ke'
    ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'newsletter',
    'shop',
   
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shopping.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'template')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'shopping.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dtechnol_myshop',
        'USER': 'dtechnol_admin',
        'PASSWORD': '0717828927@Dan',
        'HOST': 'http://dtechnologies.co.ke/',
        'PORT': '3306',
  }
}
'''


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]

#after informing django where to get the static files, then we inform it where to store the files 
#assets is a random name we have given that folder

STATIC_ROOT=os.path.join(BASE_DIR,'assets')

#os.path.join(BASE_DIR,'media')

MEDIA_URL='public_html/media/'
MEDIA_ROOT = "/home2/dtechnol/public_html/media/"


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'danielnjama2015@gmail.com'
EMAIL_HOST_PASSWORD = 'kqygvqplxmhqzufd'
EMAIL_USE_TLS = True


LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'



'''
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  
EMAIL_HOST = 'http://www.dtechnologies.co.ke/'
EMAIL_HOST_USER = 'dtechnol@dtechnologies.co.ke'
EMAIL_HOST_PASSWORD = '0717828927@Dan'
DEFAULT_FROM_EMAIL = 'dtechnol@dtechnologies.co.ke'
SERVER_EMAIL = 'http://www.dtechnologies.co.ke/'
EMAIL_PORT = 587
EMAIL_USE_TLS = False
'''