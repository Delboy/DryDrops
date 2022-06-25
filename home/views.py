from django.shortcuts import render
from django.conf import settings

from products.models import Product

# Create your views here.


def index(request):
    """ A view to return the index page """
    top_products = Product.objects.all().exclude(rating=None).order_by(
        '-rating', '-review_count')
    hot_products = Product.objects.filter(featured=True)
    hot_products_length = len(hot_products)
    delivery = settings.STANDARD_DELIVERY

    context = {
        'top_products': top_products,
        'hot_products': hot_products,
        'hot_products_length': hot_products_length,
        'delivery': delivery,
    }
    return render(request, 'home/index.html', context)
