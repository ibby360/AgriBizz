from django.shortcuts import render
from products.models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def products(request):
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
    }    
    return render(request, 'products/products.html', context)

def product_details(request):
    # product_item = Product.objects.get()
    context = {
        # 'item': product_item,
    }
        
    return render(request, 'products/product_details.html', context)
