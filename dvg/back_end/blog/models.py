from django.db import models
from django.conf import settings

# Create your models here.

class Profilr(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    website = models.URLField(blank=True)
    bio = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return self.user.get_username()