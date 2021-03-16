from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# Create your models here.
class Core(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='core')
    slug = models.SlugField(max_length=100, unique=True, editable=False)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)

    def get_absolute_urls(self):
        return reverse('core:single', kwargs={'slug': self.slug})
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-published']