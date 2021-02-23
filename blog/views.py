from django.shortcuts import get_object_or_404, render
from blog.models import BlogPost

# Create your views here.


def farming_practice(request):
    queryset = BlogPost.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'farming_practice.html', context)


def practice_details(request):
    return render(request, 'practice_details.html', {})
