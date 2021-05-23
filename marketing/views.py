from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from marketing.models import PostProduct
from marketing.forms import SellProduct

from django.contrib import messages

# Create your views here.


def market(request):
    products = PostProduct.objects.order_by('-date_created')
    context = {
        'products': products
    }
    return render(request, 'marketing/market.html', context)


def post_product(request):
    if request.method == "POST":
        form = SellProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('market')

        else:
            messages.error(request, "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    else:    
        form = SellProduct()
    context = {
        'form': form,
    }
    return render(request, 'marketing/post_product.html', context)


def single_product(request, pk):
    item = PostProduct.objects.get(pk=pk)
    products = PostProduct.objects.order_by('date_created')[:4]

    context = {
        'item': item,
        'products': products
    }
    return render(request, 'marketing/single_product.html', context)
