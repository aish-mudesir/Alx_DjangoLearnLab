
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom user model extending AbstractUser.
    Adds additional fields:
    - bio: short biography of the user
    - profile_picture: profile image of the user
    - followers: ManyToMany relationship to itself to track followers/following
    """
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    followers = models.ManyToManyField(
        'self', symmetrical=False, related_name='following', blank=True
    )

    def __str__(self):
        return self.username
