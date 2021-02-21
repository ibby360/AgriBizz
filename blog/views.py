from django.shortcuts import get_object_or_404, render
from blog.models import BlogPost

# Create your views here.


def farming_practice(request):
    return render(request, 'farming_practice.html', {})


def practice_details(request):
    return render(request, 'practice_details.html', {})
