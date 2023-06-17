from django.db import models
from django.contrib.auth.models import User

User._meta.get_field("email")._unique = True  # type: ignore


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars")
    osm_profile_link = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}'s profile"
