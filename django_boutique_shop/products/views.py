from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    return render(request, 'layout.html')

def sale(request):
    # Get all products that are on sale
    products_on_sale = Product.objects.filter(is_on_sale = True)
    products_with_images = {
        product: product.images.all() for product in products_on_sale
    }
    context = {
        'products_with_images': products_with_images,
    }
    return render(request, 'sale.html', context)

def lawn(request):
    lawn_products = Product.objects.filter(is_on_sale = False, product_type__name = 'Lawn')
    products_with_images = {
        product: product.images.all() for product in lawn_products
    }
    context = {
        'products_with_images': products_with_images,
    }
    return render(request, 'lawn.html', context)

def ocassion_wear(request):
    ocassion_products = Product.objects.filter(is_on_sale = False, product_type__name = 'Ocassion Wear')
    products_with_images = {
        product: product.images.all() for product in ocassion_products
    }
    context = {
        'products_with_images': products_with_images,
    }
    return render(request, 'ocassion_wear.html', context)

def summer_wear(request):
    summer_products = Product.objects.filter(is_on_sale = False, product_type__name = 'Summer Wear')
    products_with_images = {
        product: product.images.all() for product in summer_products
    }
    context = {
        'products_with_images': products_with_images,
    }
    return render(request, 'summer_wear.html', context)

def winter_wear(request):
    winter_products = Product.objects.filter(is_on_sale = False, product_type__name = 'Winter Wear')
    products_with_images = {
        product: product.images.all() for product in winter_products
    }
    context = {
        'products_with_images': products_with_images,
    }
    return render(request, 'winter_wear.html', context)