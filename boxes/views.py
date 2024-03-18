from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def all_products(request):
    """"
    A view to show individual boxes product details
    """
    
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_sku):
    """"
    A view to show all boxes
    """
    
    product = get_object_or_404(Product, pk=product_sku)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)