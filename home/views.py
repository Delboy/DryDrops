from django.shortcuts import render
from django.conf import settings

from products.models import Product

# Create your views here.


def index(request):
    """ A view to return the index page """
    top_products_minus = Product.objects.all().order_by('-rating')
    top_products_plus = Product.objects.all().order_by('rating')
    delivery = settings.STANDARD_DELIVERY

    context = {
        'top_products_plus': top_products_plus,
        'top_products_minus': top_products_minus,
        'delivery': delivery,
    }
    return render(request, 'home/index.html', context)
