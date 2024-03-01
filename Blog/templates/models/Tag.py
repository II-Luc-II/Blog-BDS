from django.db import models
# from blog.models import Post


class Tag(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    # posts = models.ManyToManyField(Post)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
