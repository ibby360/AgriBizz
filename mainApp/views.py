from django.shortcuts import render
from mainApp.models import Newsletter
from blog.models import BlogPost, News





# Create your views here.


def index(request):
    practice_post = BlogPost.objects.filter(featured=True)
    news_post = News.objects.filter(featured_news=True)
    list_news = News.objects.order_by('-date_created').exclude(featured_news=True)
    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Newsletter()
        new_signup.email = email
        new_signup.save()

    
    context = {
        'object_list': practice_post,
        'featured_news': news_post,
        'news_list': list_news
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html',)
