from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nom")
    description = models.CharField(max_length=255, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Enregistré le ")

    def __str__(self) -> str:
        return self.name



