from django.shortcuts import render
import mainApp.models as app_model
from blog.models import BlogPost
from django.views import generic



# Create your views here.


def index(request):
    practice_post = BlogPost.objects.filter(featured=True)
    context = {
        'object_list': practice_post
    }
    return render(request, 'index.html', context)
