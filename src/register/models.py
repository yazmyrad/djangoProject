from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user     = models.OneToOneField(User, on_delete=models.CASCADE)
    bioText  = models.TextField(max_length=150, blank=True, default='')
    avatar   = models.ImageField(upload_to ='avatars/%Y/%m/%d/', blank=True, null=True, default=None)

    def __str__(self):
        return self.user.username