from django.shortcuts import render
from mainApp.models import Newsletter
from blog.models import BlogPost
from django.views import generic



# Create your views here.


def index(request):
    practice_post = BlogPost.objects.filter(featured=True)
    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Newsletter()
        new_signup.email = email
        new_signup.save()

    
    context = {
        'object_list': practice_post
    }
    return render(request, 'index.html', context)
