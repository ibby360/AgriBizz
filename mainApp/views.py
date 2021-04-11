from django.db.models import Q
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from mainApp.models import Newsletter, Contact
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
        'news_list': list_news,
    }
    return render(request, 'index.html', context)


def thank_you(request):
    return render(request, 'thank_you.html', )

# Contact view page function    
def contact(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        return HttpResponseRedirect('thank_you')
        

    return render(request, 'contact.html',)

    
# About us page view function
def about_us(request):
    return render(request, 'about.html', )

# 404 error page view function
def error_404(request, exception):
        context = {}
        return render(request,'404.html', context)

# Search result view function
def search_page(request):
    queryset = BlogPost.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search.html', context)