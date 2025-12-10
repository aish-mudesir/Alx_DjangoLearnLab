from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Accounts app endpoints
    path('api/accounts/', include('accounts.urls')),

    # Posts app endpoints
    path('api/', include('posts.urls')),
]
