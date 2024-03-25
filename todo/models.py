from django.db import models

# Create your models here.
from django.conf import settings

class Todo(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField( blank=True)
    limit = models.DateField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   verbose_name="投稿者",
                                   on_delete=models.CASCADE)
    created_at = models.DateTimeField('投稿日', auto_now_add=True)
    created_at = models.DateTimeField('更新日', auto_now=True)

    def _str__(self):
        return self.title

