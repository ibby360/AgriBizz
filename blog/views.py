from django.core import paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.query_utils import PathInfo
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from blog.models import BlogPost, News

# Create your views here.

# View for the farming practicies page
def farming_practice(request):
    post_list = BlogPost.objects.all()
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
    }
    return render(request, 'farming_practice.html', context)

# View for the practice details page
def practice_details(request,):
    post = BlogPost.objects.get(id = 2)
    context = {
        'post': post,
    }
    return render(request, "practice_details.html", context)

# View for the news page
def news_view (request):
    news_list = News.objects.all()
    pratice_post = BlogPost.objects.filter(featured=True)[:4]
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
        'object_list':pratice_post
    }
    return render(request, "news.html", context) 