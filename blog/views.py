from django.core import paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.db.models.fields import SlugField
# from django.db.models.query_utils import PathInfo
# from django.http.response import Http404
from django.shortcuts import render
from blog.models import BlogPost, News
# from .forms import CommentForm

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


def practice_details(request, slug):
    post = BlogPost.objects.get(slug=slug)
    # comments = BlogPost.comments.filter(active=True)
    # new_comment = None
    # # comment posted
    # if request.method == 'POST':
    #     comment_form = CommentForm(data=request.POST)
    #     if comment_form.is_valid():
    #         # create comment object but don't save to database yet
    #         new_comment = comment_form.save(commit=False)
    #         # Assign the current post to the comment
    #         new_comment.post = post
    #         # Save the comment to the database
    #         new_comment.save()

    #     else:
    #         comment_form = CommentForm()
    context = {
        'post': post,
        # 'comments': comments,
        # 'new_comment': new_comment,
        # 'comment_form': comment_form,
    }
    return render(request, "practice_details.html", context)

# View for the news page


def news_view(request):
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
        'object_list': latest_pratice_post

    }
    return render(request, "news.html", context)
