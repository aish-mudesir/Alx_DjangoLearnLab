# Custom User Model
AUTH_USER_MODEL = 'accounts.CustomUser'

# Make sure 'accounts' is in INSTALLED_APPS
INSTALLED_APPS = [
    # default apps...
    'django.contrib.admin',
    'django.contrib.auth',
    # other apps...
    'accounts',
]
