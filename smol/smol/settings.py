"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "k&ndet-+-&(yxp_hih^k9y*$hbe2p=$vzeryfj$x*&$#+0-$sx"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    "192.168.178.20",
    "localhost",
    "127.0.0.1",
    os.environ.get("HOST", "smol.localhost"),
]
DEFAULT_CHARSET = "utf-8"


# Application definition

INSTALLED_APPS = [
    "viewer.apps.ViewerConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    # 'corsheaders',
    "debug_toolbar",
]

MIDDLEWARE = [
    # 'django.middleware.cache.UpdateCacheMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    # 'django.middleware.csrf.CsrfViewMiddleware',
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # 'django.middleware.cache.FetchFromCacheMiddleware'
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False
ROOT_URLCONF = "smol.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "viewer.context_processors.random_video",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "smol.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

sqlite_file = Path("/srv/data/smol/local_media/smol/db")
sqlite_file.mkdir(exist_ok=True, parents=True)
sqlite_file = sqlite_file / "smol.db"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(sqlite_file),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "CET"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

PROJECT_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT_alt = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = "/static/"
STATIC_ROOT = PROJECT_ROOT/"static"


def always_true(request):
    return True


SHOW_TOOLBAR_CALLBACK = always_true
INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
    "192.168.178.20",
    "192.168.178.20",
    os.environ.get("HOST", "smol.localhost"),
]

SITE_ID = 1

PREVIEW_IMAGES = 15

MEDIA_URL = "/viewer/images/"
MEDIA_ROOT = BASE_DIR/"media/"
MEDIA_DIR = BASE_DIR/"local_media"

THUMBNAIL_DIR = STATIC_ROOT / "viewer/images/thumbnails"
PREVIEW_DIR = STATIC_ROOT / "viewer/images/previews"
if not THUMBNAIL_DIR.is_dir():
    THUMBNAIL_DIR.mkdir(exist_ok=True, parents=True)
if not PREVIEW_DIR.is_dir():
    PREVIEW_DIR.mkdir(exist_ok=True, parents=True)

VIDEO_SUFFIXES = [
    ".mp4",
    ".mov",
    ".wmv",
    ".avi",
    ".flv",
    ".mkv",
    ".webm",
    ".gp3",
    ".ts",
    ".mpeg",
]
IMAGE_SUFFIXES = [
    ".jpg",
    ".jpeg",
    ".png",
    ".JPG",
    ".tiff",
    ".gif",
    ".bmp",
]
