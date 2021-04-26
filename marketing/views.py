from django.shortcuts import render
from marketing.models import PostProduct

# Create your views here.
def market(request):
    products = PostProduct.objects.all()
    context = {
        'products': products
    }
    return render(request, 'marketing/market.html', context)

def post_product(request):
    if request.method == 'POST':
        post_product = PostProduct()

        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        region = request.POST.get('region')
        location = request.POST.get('location')

        post_product.full_name = full_name
        post_product.email= email
        post_product.phone_number = phone_number
        post_product.region = region
        post_product.location = location

        product_name = request.POST.get('product_name')
        scale = request.POST.get('scale')
        amount = request.POST.get('amount')
        price = request.POST.get('price')

        post_product.product_name = product_name
        post_product.scale = scale
        post_product.quantity = amount
        post_product.price = price


        post_product.save()

    # region = Person.objects.get(region)

    context = {
        # 'region': region,
    }
    return render(request, 'marketing/post_product.html', context)

def single_product(request, pk):
    item = PostProduct.objects.get(pk=pk)

    context = {
        'item': item
    }
    return render(request, 'marketing/single_product.html', context)