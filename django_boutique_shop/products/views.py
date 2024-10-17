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