from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title   = models.CharField(max_length=200)
    content = models.TextField()
    author  = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    source  = models.URLField(max_length=200, blank=True, null=True)
    slug    = models.SlugField(unique=True, null=False)
    tags    = TaggableManager()
    category= models.ForeignKey('Categories', null=True, on_delete=models.SET_NULL)
    datepubl= models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.pk: 
            self.datepubl = timezone.now()
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog', kwargs={'blog_id': self.pk})
    
class Categories(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
