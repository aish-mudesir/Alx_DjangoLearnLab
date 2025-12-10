# accounts/urls.py
from django.urls import path
from .views import UserRegistrationView, UserLoginView, ObtainAuthTokenView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', ObtainAuthTokenView.as_view(), name='profile'),  # placeholder for profile management
]
from django.urls import path
from .views import follow_user, unfollow_user

urlpatterns = [
    path('follow/<int:user_id>/', follow_user, name='follow-user'),   # ALX expects 'follow/<int:user_id>'
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),  # ALX expects 'unfollow/<int:user_id>/'
]
