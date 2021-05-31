from shop.models import Product
from django.shortcuts import render
from orders.models import OrderItem
from orders.forms import OrderCreateForm
from cart.cart import Cart
# Create your views here.


def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            # clear the cart
            cart.clear()

            return render(request, 'orders/successful.html', {'order': order})
    else:
        form = OrderCreateForm()

    context = {
        'cart': cart,
        'form': form
    }
    return render(request, 'orders/checkout.html', context)