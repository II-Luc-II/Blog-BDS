from django.db import models


class Contact(models.Model):
    civility = models.CharField(max_length=60, verbose_name="Civilité")
    name = models.CharField(max_length=60, verbose_name="Nom")
    email = models.EmailField()
    subject = models.CharField(max_length=255, verbose_name="Sujet")
    message = models.TextField()
    file = models.FileField(upload_to='contacts/%Y/%m/%d/, blank=True, null=True', verbose_name="Fichier")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")

