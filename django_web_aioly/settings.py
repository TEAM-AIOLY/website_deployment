"""
Django settings for django_web_aioly project.
"""

import os
from pathlib import Path
import gettext



BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-lta%!6bqdqfkapa4fqfrj2-p=%vgas9h9*^nr^-w@z-o)9(-08'

DEBUG = False
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_distill',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # ✅ Ajoute ceci pour activer la détection et le changement de langue
    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_web_aioly.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # ⚠️ nécessaire pour {% url 'set_language' %}
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_web_aioly.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌍 INTERNATIONALISATION
LANGUAGE_CODE = 'fr'

LANGUAGES = [
    ('fr', 'Français'),
    ('en', 'English'),
]

USE_I18N = True
USE_TZ = True
TIME_ZONE = 'UTC'

# ✅ Dossier où seront stockés les fichiers .po et .mo
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

for path in LOCALE_PATHS:
    en_mo = os.path.join(path, 'en', 'LC_MESSAGES', 'django.mo')
    print("🗂 Checking translation file:", en_mo, "→ Exists?", os.path.exists(en_mo))

# 🖼️ FICHIERS STATIQUES
if 'distill' in os.environ.get('DJANGO_SETTINGS_MODULE', ''):
    STATIC_URL = '/website_deployment/static/'
else:
    STATIC_URL = '/website_deployment/static/'

DISTILL_STATIC = True
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

print("LANGUAGES:", LANGUAGES)
print("LOCALE_PATHS:", LOCALE_PATHS)
print("LANGUAGE_CODE:", LANGUAGE_CODE)