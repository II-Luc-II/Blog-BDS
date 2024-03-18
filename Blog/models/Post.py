from django.db import models
from django.contrib.auth.models import User
from Blog.models import Category, Tag
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=60 ,verbose_name="Titre")
    slug = models.SlugField(max_length=255)
    content = models.TextField(verbose_name="Article")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Auteur")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Catégorie")
    is_published = models.BooleanField(default=False, verbose_name="Publié")
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Enregistré le ")
    image = models.ImageField(upload_to='posts/%Y/%m/%d/', blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
