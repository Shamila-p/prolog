"""
Django settings for prolog project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o_&c^z&f)ug*4(fy3^7%7assew9&#k99@=+$9-0-36$k7_9&ay'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'access.apps.AccessConfig',
    'member.apps.MemberConfig',
    'common.apps.CommonConfig',
    'course.apps.CourseConfig',
    'StudyMaterials.apps.StudymaterialsConfig',
    'assignment.apps.AssignmentConfig',
    'attendence.apps.AttendenceConfig',
    'mark.apps.MarkConfig',
    'notifications.apps.NotificationsConfig',
    'fees.apps.FeesConfig',
    'certificates.apps.CertificatesConfig',
    'sms.apps.SmsConfig',
    'dashboard.apps.DashboardConfig'
]
AUTH_USER_MODEL = 'member.User'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'prolog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'course/templates'),
            os.path.join(BASE_DIR,'access/templates'),
            os.path.join(BASE_DIR,'common/templates'),
            os.path.join(BASE_DIR,'member/templates'),
            os.path.join(BASE_DIR,'StudyMaterials/templates'),
            os.path.join(BASE_DIR,'assignment/templates'),
            os.path.join(BASE_DIR,'attendence/templates'),
            os.path.join(BASE_DIR,'mark/templates'),
            os.path.join(BASE_DIR,'notifications/templates'),
            os.path.join(BASE_DIR,'fees/templates'),
            os.path.join(BASE_DIR,'certificates/templates'),
            os.path.join(BASE_DIR,'sms/templates'),
            os.path.join(BASE_DIR,'dashboard/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'course.context_processor.is_tutor'
            ],
        },
    },
]

WSGI_APPLICATION = 'prolog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'prolog',
        'USER':'root',
        'PASSWORD':'1234',
        'HOST':'127.0.0.1'
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

LOGIN_URL = 'login'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER ='prolog586@gmail.com'
EMAIL_HOST_PASSWORD = 'cltuqmwhcqehuskc'
DOMAIN_URL='http://127.0.0.1:8000/'