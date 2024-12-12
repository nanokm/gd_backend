import enum
from pathlib import Path

from django.conf import settings
from environs import Env

BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
env.read_env()

SECRET_KEY = env.str("SECRET_KEY", "django-insecure-feef@8-q5-uq(8!a0t&(ww2djg0vtr*ys0^g#8f3d-*qfa*h-m")


############################################################################
############################################################################
#########################        APP SETTINGS      #########################
############################################################################
############################################################################
AUTH_USER_MODEL = "user.GDUser"
APP_SRID = 4326
MAX_DISTANCE_FROM_POINT_KM = 10
OSM_DB_NAME = "osm"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "knox.auth.TokenAuthentication",
    ]
}

REST_KNOX = {
    "USER_SERIALIZER": "shared.serializers.GDUserSerializer",
}

INTERNAL_IPS = [
    "127.0.0.1",
    "0.0.0.0",
    "localhost",
    "*",
]

DATABASE_ROUTERS = ["gd_backend.db_routers.OSMRouter"]
SESSION_ENGINE = "django.contrib.sessions.backends.cache"

############################################################################
############################################################################
#########################            END           #########################
############################################################################
############################################################################


DEBUG = env.bool("DEBUG", True)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*", "localhost"])


THIRD_PARTY_APPS = [
    "rest_framework",
    "django_filters",
    "knox",
]
THIRD_PARTY_DEV_APPS = ["debug_toolbar"]
PROJECT_APPS = [
    "apps.user.apps.UserConfig",
    "apps.map.apps.MapConfig",
    "apps.filterbar.apps.FilterbarConfig",
    "apps.shared.apps.SharedConfig",
    "apps.org.apps.OrgConfig",
]
INSTALLED_APPS = (
    [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.gis",
    ]
    + THIRD_PARTY_DEV_APPS
    + THIRD_PARTY_APPS
    + PROJECT_APPS
)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "gd_backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "gd_backend.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("POSTGRES_DB", "postgres"),
        "USER": env.str("POSTGRES_USER", "user"),
        "PASSWORD": env.str("POSTGRES_PASSWORD", "password"),
        "HOST": env.str("POSTGRES_HOST", "localhost"),
        "PORT": env.str("POSTGRES_PORT", "5432"),
    },
    OSM_DB_NAME: {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "osmtest",
        "USER": env.str("POSTGRES_USER", "user"),
        "PASSWORD": env.str("POSTGRES_PASSWORD", "password"),
        "HOST": env.str("POSTGRES_HOST", "localhost"),
        "PORT": env.str("POSTGRES_PORT", "5432"),
    },
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": env.str("REDIS_URL", "redis://localhost:6379/"),
        "KEY_PREFIX": "imdb",
        "TIMEOUT": 60 * 15,  # in seconds: 60 * 15 (15 minutes)
    }
}

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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
