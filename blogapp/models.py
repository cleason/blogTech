from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = RichTextField(blank=True, verbose_name="Contenu")
    image = models.ImageField(upload_to = 'images', blank=True)
    
    def __str__(self):
        return self.title


    # On rajoute une classe Meta pour préciser notre modèle
    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"

