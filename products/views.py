from django.shortcuts import render
from products.models import Product 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import BlogPost


# Create your views here.
def products(request):
    posts = BlogPost.objects.order_by('-date_created')[:3]
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 6)
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
    return render(request, 'products/products.html', context)
    

def product_details(request, slug):
    product = Product.objects.get(slug = slug)
    related = Product.objects.order_by('-date_created')[:4]
    context = {
        'item': product,
        'related': related,
    }
        
    return render(request, 'products/product_details.html', context)
