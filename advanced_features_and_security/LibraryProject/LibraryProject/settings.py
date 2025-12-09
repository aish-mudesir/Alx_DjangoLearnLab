"""
"""
Django settings (security-minded example) for advanced_features_and_security.
Keep SECRET_KEY secret and set DEBUG=False in production via environment variables.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# WARNING: Replace with a secure secret key in production (do not share).
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "django-insecure-dev-key")

# DEBUG should be False in production. Use env var to toggle in different environments.
DEBUG = os.environ.get("DJANGO_DEBUG", "False").lower() in ("1", "true", "yes")

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost").split(",")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "bookshelf",
    "accounts",  # if you have custom user app
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # optionally enable WhiteNoise if serving static files in production
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",

    # CSRF protection middleware (enabled by default)
    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",

    # Clickjacking protection
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # Custom CSP middleware (below) - add near the end so it can modify responses
    "advanced_features_and_security.security_middleware.ContentSecurityPolicyMiddleware",
]

ROOT_URLCONF = "advanced_features_and_security.urls"

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

WSGI_APPLICATION = "advanced_features_and_security.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ---------------------
# Security settings
# ---------------------
# Prevent reflected XSS by enabling the browser XSS filter
SECURE_BROWSER_XSS_FILTER = True

# Prevent clickjacking
X_FRAME_OPTIONS = "DENY"

# Tell browsers not to sniff content types — prevents MIME confusion attacks
SECURE_CONTENT_TYPE_NOSNIFF = True

# When https, ensure cookies are only sent via HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# HSTS: tell browsers to only use HTTPS
# Only enable with HTTPS in production and carefully choose seconds
SECURE_HSTS_SECONDS = int(os.environ.get("DJANGO_SECURE_HSTS_SECONDS", "0"))
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = os.environ.get("DJANGO_SECURE_SSL_REDIRECT", "False").lower() in ("1", "true")

# ---------------------
# Internationalization & static
# ---------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
