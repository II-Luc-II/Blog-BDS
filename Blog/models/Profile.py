from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    description = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name="Utilisateur")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Enregistré le")

    def __str__(self):
        return self.description
