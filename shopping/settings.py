import os

#for sendgrid
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a#)d3hat2$ghq1*qj7akhcs^@e9%qq+@^!^9v$*1-=w3^#99io'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

"""
ALLOWED_HOSTS = [
    'http://www.dtechnologies.co.ke',
    'dtechnologies.co.ke',
    'www.dtechnologies.co.ke'
    ]
"""

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_social_share',
    'storages',
    'blog',
    'ckeditor',
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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]

#after informing django where to get the static files, then we inform it where to store the files 
#assets is a random name we have given that folder

#STATIC_ROOT=os.path.join(BASE_DIR,'assets')



MEDIA_URL='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'static/media')

'''
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'danielnjama2015@gmail.com'
EMAIL_HOST_PASSWORD = 'kqygvqplxmhqzufd'
EMAIL_USE_TLS = True
'''


LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'

#EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
#SENDGRID_API_KEY = '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'

#SENDGRID_SANDBOX_MODE_IN_DEBUG=False

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Toggle sandbox mode (when running in DEBUG mode)
#SENDGRID_SANDBOX_MODE_IN_DEBUG=True
# echo to stdout or any other file-like object that is passed to the backend via the stream kwarg.
'''
SENDGRID_ECHO_TO_STDOUT=True
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_USE_TLS = True
'''



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  
#EMAIL_BACKEND = 'django_ses.SESBackend'
EMAIL_HOST = 'mail.dtechnologies.co.ke'
EMAIL_HOST_USER = 'client@dtechnologies.co.ke'
EMAIL_HOST_PASSWORD = '0717828927@Dan'
DEFAULT_FROM_EMAIL = ""
EMAIL_PORT = 26
EMAIL_USE_TLS = False
#EMAIL_USE_TLS = True
#EMAIL_USE_SSL = False


STATIC_URL = '/static/'




""" AWS_ACCESS_KEY_ID = 'AKIAY4D4KK6WUBMZAD5K'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = "techdemo5115"
#AWS_STORAGE_BUCKET_NAME = "dtechnologies"
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
AWS_DEFAULT_ACL='public-read'
#AWS_DEFAULT_ACL = None


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'shopping.storage_backends.MediaStorage' """




"""
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <AllowedMethod>POST</AllowedMethod>
        <AllowedMethod>PUT</AllowedMethod>
        <AllowedHeader>*</AllowedHeader>
    </CORSRule>
</CORSConfiguration>


"""