from django.shortcuts import render
from django.conf import settings

from products.models import Product

# Create your views here.


def index(request):
    """ A view to return the index page """
    top_products = Product.objects.all().exclude(rating=None).order_by(
        '-rating')
    delivery = settings.STANDARD_DELIVERY

    context = {
        'top_products': top_products,
        'delivery': delivery,
    }
    return render(request, 'home/index.html', context)
