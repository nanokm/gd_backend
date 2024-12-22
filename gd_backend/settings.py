import enum
import os
from pathlib import Path

from django.conf import settings
from django.utils.translation import gettext_lazy as _
from environs import Env

BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
env.read_env()

SECRET_KEY = env.str("SECRET_KEY", "django-insecure-feef@8-q5-uq(8!a0t&(ww2djg0vtr*ys0^g#8f3d-*qfa*h-m")
DEBUG = env.bool("DEBUG", True)

#########################        APP SETTINGS      #########################
AUTH_USER_MODEL = "user.GDUser"
APP_SRID = 4326
MAX_DISTANCE_FROM_POINT_KM = 3
OSM_DB_NAME = "osm"
OSM_POINT_TABLE_POINT = "planet_osm_point"


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "knox.auth.TokenAuthentication",
    ]
}

REST_KNOX = {
    "USER_SERIALIZER": "shared.serializers.GDUserSerializer",
}

DATABASE_ROUTERS = ["gd_backend.db_routers.OSMRouter"]
SESSION_ENGINE = "django.contrib.sessions.backends.cache"

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

LANGUAGES = [
    ("pl", _("Polish")),
    ("en", _("English")),
]

LANGUAGE_CODE = "pl"

LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]

OSM_CATEGORY_MAPPING = {
    "books": {"column": "shop", "value": "books"},
    "restaurant": {"column": "amenity", "value": "restaurant"},
    "cafe": {
        "column": "amenity",
        "value": "cafe",
    },
    "fast_food": {
        "column": "amenity",
        "value": "fast_food",
    },
    "convenience": {
        "column": "shop",
        "value": "convenience",
    },
    "pharmacy": {
        "column": "amenity",
        "value": "pharmacy",
    },
    "gym": [
        {
            "column": "leisure",
            "value": "fitness_centre",
        },
        {"column": "amenity", "value": "gym"},
        {"column": "sport", "value": "fitness"},
        {"column": "leisure", "value": "sports_hall"},
        {"column": "sport", "value": "multi"},
        {"column": "leisure", "value": "bowling_alley"},
        {"column": "leisure", "value": "ice_rink"},
        {"column": "leisure", "value": "fitness_station"},
        {"column": "leisure", "value": "sports_centre"},
    ],
    "community_centre": [
        {
            "column": "amenity",
            "value": "community_centre",
        },
        {
            "column": "tourism",
            "value": "museum",
        },
        {"column": "tourism", "value": "gallery"},
        {"column": "shop", "value": "antiques"},
        {
            "column": "amenity",
            "value": "theatre",
        },
    ],
    "atm": {"column": "amenity", "value": "atm"},
    "religion": {"column": "religion", "value": "religion"},
}

OSM_CATEGORY_LIST = [key.lower() for key in OSM_CATEGORY_MAPPING.keys()]


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
]

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": "1079725403294-8vmqev45k1qti5pfudak8ll6dpiu0leg.apps.googleusercontent.com",
            "secret": "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",
            "key": "",
        },
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    }
}

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_ON_GET = True
SOCIALACCOUNT_LOGIN_ON_GET = True


PELIAS_ENDPOINT = env.str("PELIAS_ENDPOINT", "http://pelias_api:4000/")

if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

############################################################################

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*", "localhost"])


THIRD_PARTY_APPS = [
    "rest_framework",
    "django_filters",
    "knox",
    "phonenumber_field",
    "rest_framework_gis",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
]

PROJECT_APPS = ["apps.user", "apps.map", "apps.shared", "apps.org", "apps.offer", "apps.prices", "apps.geocoding"]

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
    + THIRD_PARTY_APPS
    + PROJECT_APPS
)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "gd_backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": env.str("POSTGRES_DB", "postgres"),
        "USER": env.str("POSTGRES_USER", "user"),
        "PASSWORD": env.str("POSTGRES_PASSWORD", "password"),
        "HOST": env.str("POSTGRES_HOST", "localhost"),
        "PORT": env.str("POSTGRES_PORT", "5432"),
    },
    OSM_DB_NAME: {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": OSM_DB_NAME,
        "USER": env.str("POSTGRES_USER", "user"),
        "PASSWORD": env.str("POSTGRES_PASSWORD", "password"),
        "HOST": env.str("POSTGRES_HOST", "localhost"),
        "PORT": env.str("POSTGRES_PORT", "5432"),
    },
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": env.str("REDIS_URL", "redis://redis:6379/"),
        "KEY_PREFIX": "gd",
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

TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = "static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
LOGIN_URL = "/admin/login/"
