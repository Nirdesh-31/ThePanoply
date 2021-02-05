from django.shortcuts import render
from .models import Product, ExploreProduct


def index(request):
    products = ExploreProduct.objects.all()
    context = {'products': products}
    return render(request, 'store/index.html', context)


def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/product.html', context)


def about(request):
    products = ExploreProduct.objects.all()
    context = {'products': products}
    return render(request, 'store/about.html', context)
