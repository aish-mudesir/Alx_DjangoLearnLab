
from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        # Create groups and assign permissions
        Group.objects.get_or_create(name='Editors')
        Group.objects.get_or_create(name='Viewers')
        Group.objects.get_or_create(name='Admins')
