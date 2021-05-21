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
    file_path = 'products/images{author_id}/{crop_name}-{filename}'.format(
        author_id=str(instance.author.id), crop_name=str(instance.crop_name), filename=filename
    )
    return file_path

class Crops(models.Model):
    STATUS_CHOICE = (('draft', 'Draft'), ('published', 'Published'),)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default='')
    category = models.CharField(max_length=150, blank=True)
    crop_name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, unique=True)
    thumbnail = models.ImageField(
        upload_to=upload_location, null=True, blank=True)
    crop_description = HTMLField(blank=True)
    varieties = HTMLField(blank=True)
    processing_type = HTMLField(blank=True)
    quality_factor = HTMLField(blank=True)
    price_factor = HTMLField(blank=True)
    publish = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(verbose_name='date-published',auto_now_add=True)
    publish_date =models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')


    class Meta:
        ordering = ('-publish',)
        verbose_name = 'crop'
        verbose_name_plural = 'crops'

    def __str__(self):
        return self.crop_name
