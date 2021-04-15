from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify
from django.urls import reverse
from blog.models import Author

from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# Media files location


def upload_location(instance, filename):
    file_path = 'products/images{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id), title=str(instance.title), filename=filename
    )
    return file_path


class Category(models.Model):
    title = models.CharField(max_length=20)

    class meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS_CHOICE = (('draft', 'Draft'), ('published', 'Published'),)
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, unique=True)
    categories = models.ManyToManyField(Category)
    thumbnail = models.ImageField(
        upload_to=upload_location, null=True, blank=True)
    varieties = HTMLField()
    processing_type = HTMLField()
    quality_factor = HTMLField()
    priec_factor = HTMLField()
    publish = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(verbose_name='date-published',auto_now_add=True)
    publish_date =models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')


    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.product_name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.product_name
