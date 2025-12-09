import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY should come from env in production
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "unsafe-dev-secret")

# Turn off DEBUG in production
DEBUG = os.environ.get("DJANGO_DEBUG", "False").lower() in ("1", "true", "yes")

# Must set to your domain(s) in production (comma separated)
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

INSTALLED_APPS = [
    # default apps...
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # your apps...
    "bookshelf",
    "accounts",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    # clickjacking protection:
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # (optionally) CSP middleware if you added one:
    # "advanced_features_and_security.security_middleware.ContentSecurityPolicyMiddleware",
]

# Use SECURE_PROXY_SSL_HEADER if you're behind a reverse proxy (nginx) that sets X-Forwarded-Proto
# Example: ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# ===========================
# HTTPS & cookies settings
# ===========================
# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = os.environ.get("DJANGO_SECURE_SSL_REDIRECT", "True").lower() in ("1", "true")

# HSTS (HTTP Strict Transport Security)
# 31536000 seconds = 1 year; set to 0 initially if you are testing
SECURE_HSTS_SECONDS = int(os.environ.get("DJANGO_SECURE_HSTS_SECONDS", "31536000"))
SECURE_HSTS_INCLUDE_SUBDOMAINS = os.environ.get("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", "True").lower() in ("1", "true")
SECURE_HSTS_PRELOAD = os.environ.get("DJANGO_SECURE_HSTS_PRELOAD", "True").lower() in ("1", "true")

# Make cookies secure: only sent over HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Prevent browsers from MIME-sniffing content types
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable the browser XSS filter
SECURE_BROWSER_XSS_FILTER = True

# Prevent site from being embedded in frames (clickjacking protection)
X_FRAME_OPTIONS = "DENY"

# Other recommended settings
# Ensure you serve cookies with `SameSite` as appropriate:
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SAMESITE = "Lax"

# Static / media (example)
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# rest of your settings...
