from django.shortcuts import render

from products.models import Product

# Create your views here.


def index(request):
    """ A view to return the index page """
    top_products = Product.objects.all().order_by('-rating')
    context = {
        'top_products': top_products,
    }
    return render(request, 'home/index.html', context)
