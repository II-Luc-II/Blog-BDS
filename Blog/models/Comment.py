from django.db import models
from django.contrib.auth.models import User

from Blog.models.Post import Post


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Auteur")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Article")
    note = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Enregistrer le")

    def __str__(self) -> str:
        return self.content

    class Meta:
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"
