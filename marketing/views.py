from django.shortcuts import render

# Create your views here.
def market(request):
    return render(request, 'marketing/market.html', {})

def post_product(request):
    return render(request, 'marketing/post_product.html', {})

def single_product(request):
    return render(request, 'marketing/single_product.html', {})