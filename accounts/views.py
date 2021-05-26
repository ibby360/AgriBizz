from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user
from accounts.forms import CreateUserForm
from marketing.forms import SellProduct
from marketing.models import PostProduct

@unauthenticated_user
def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def dashboard(request):
    products = PostProduct.objects.order_by('-date_created')
    context = {
        'products': products
    }
    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='/login/')
def products(request):
    products = PostProduct.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'accounts/products.html', context)

@login_required(login_url='/login/')
def post_product(request):
    if request.method == "POST":
        form = SellProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('market')

    else:
        form = SellProduct()
    context = {
        'form': form,
    }
    return render(request, 'marketing/post_product.html', context)

@login_required(login_url='/login/')
def delete_product(request, pk):
	products = PostProduct.objects.get(pk=pk)
	if request.method == "POST":
		products.delete()
		return redirect('dashboard')

	context = {'products':products}
	return render(request, 'accounts/delete.html', context)

@login_required(login_url='/login/')
def update_product(request, pk):

	product = PostProduct.objects.get(pk=pk)
	form = SellProduct(instance=product)

	if request.method == 'POST':
		form = SellProduct(request.POST, instance=product)
		if form.is_valid():
			form.save()
			return redirect('dashboard')

	context = {'form':form}
	return render(request, 'accounts/update_product.html', context)