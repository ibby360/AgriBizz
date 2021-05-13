from django.shortcuts import render
from crops.models import Crops 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import BlogPost


# Create your views here.
def crops(request):
    posts = BlogPost.objects.order_by('-date_created')[:3]
    crops_list = Crops.objects.all()
    paginator = Paginator(crops_list, 6)
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
        'posts': posts,

    }    
    return render(request, 'crops/crops.html', context)
    

def crop_details(request, slug):
    crop = Crops.objects.get(slug = slug)
    related = Crops.objects.order_by('-date_created')[:4]
    context = {
        'crop': crop,
        'related': related,
    }
        
    return render(request, 'crops/crop_details.html', context)
