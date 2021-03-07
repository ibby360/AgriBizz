from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from django.db.models.fields.files import ImageField

from django.db.models.signals import post_delete, pre_save
from django.utils.text import slugify
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver

# Create your models here.


def upload_location(instance, filename):
    file_path = 'blog/images{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id), title=str(instance.title), filename=filename
    )
    return file_path

# Post model
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField()
    
    def __str__(self):
        return self.user.username
    

class BlogPost (models.Model):
    STATUS_CHOICE = (('draft', 'Draft'), ('published', 'Published'),)
    title = models.CharField(max_length=200,)
    overview = models.CharField(max_length=150, null=True)
    slug = models.SlugField(max_length=100, null=True, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    thumbnail = models.ImageField(upload_to=upload_location, null=True, blank=True)
    icon = ImageField(upload_to=upload_location, null=True, blank=True)
    content = HTMLField()
    publish = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name="date_published")
    date_updated = models.DateTimeField(
        auto_now=True, verbose_name="date_updated")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICE, default='draft')
    featured = models.BooleanField()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("practice_detail", kwargs={"pk": self.id})
    