from django.core import paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.http import request
from django.shortcuts import render
from blog.models import BlogPost, News, PracticeIntro, Comment
from blog.forms import CommentForm, NewsCommentForm
from django.contrib import messages
# Create your views here.

def farming_practice(request):  # View for the farming practicie page
    post_list = BlogPost.objects.all()
    introduction = PracticeIntro.objects.all()
    paginator = Paginator(post_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'introduction': introduction,
    }
    return render(request, 'blog/farming_practice.html', context)


def practice_details(request, slug):  # View for the practice details page
    post = BlogPost.objects.get(slug=slug)
    comments = post.comments.filter(active=True)
    # Comment posted
    comment_form = CommentForm(request.POST or None)
    if request.method == "POST":
        if comment_form.is_valid():
            comment_form.instance.post = post
            comment_form.save()
            messages.success(request, "Your comment was successfully uploaded. Wait for admin to aprove it.")

        else:
            comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, "blog/practice_details.html", context)


def news_view(request):  # View for the news page
    news_list = News.objects.all()
    latest_pratice_post = BlogPost.objects.order_by('-date_created')[:4]
    paginator = Paginator(news_list, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'object_list': latest_pratice_post,

    }
    return render(request, "blog/news.html", context)


def practice_intro(request,):  # Practice intro page view
    intro_page = PracticeIntro.objects.get(pk=1)
    context = {'intro_page': intro_page}
    return render(request, 'blog/practice_intro.html', context)


def news_details(request, slug):  # News details page veiw
    news = News.objects.get(slug=slug)
    comments = news.comments.filter(active=True)
    # Comment posted
    comment_form = NewsCommentForm(request.POST or None)
    if request.method == "POST":
        if comment_form.is_valid():
            comment_form.instance.news = news
            comment_form.save()
            comment_form = NewsCommentForm()
            messages.success(request, "Your comment was successfully uploaded. Wait for admin to aprove it.")

        else:
            comment_form = NewsCommentForm()
    context = {
        'news': news,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'blog/news_details.html', context)
