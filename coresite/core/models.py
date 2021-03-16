from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Core(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='core')
    slug = models.SlugField(max_length=100, unique=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)

    def get_absolute_urls(self):
        return reverse('core:single', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published']