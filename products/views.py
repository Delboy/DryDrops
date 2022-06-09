from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.db.models import Avg
from django.conf import settings

from .models import Product, Category
from review.models import Review
from .forms import ProductForm
from review.forms import ReviewForm
from profiles.models import UserProfile


# Create your views here.


def all_products(request):
    """ A view to show all products and search queries """

    products = Product.objects.all().order_by('sku')
    hot_products = Product.objects.filter(featured=True)
    delivery = settings.STANDARD_DELIVERY
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'hot_products': hot_products,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'delivery': delivery,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual products details """
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.all().filter(product=product)
    review_count = len(reviews)

    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            reviews.create(
                user=user_profile,
                product=product,
                rating=request.POST.get('rating'),
                body=request.POST.get('body')
            )
            reviews = Review.objects.all().filter(product=product)
            rating = reviews.aggregate(Avg('rating'))['rating__avg']
            product.rating = rating
            product.save()
            messages.success(request, 'Review sucessfully added')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            print(form.errors.as_data())
            messages.error(
                request,
                'Review Failed. \
                    Please check for errors or profanity and try again.'
                )
            return redirect(reverse('product_detail', args=[product_id]))
    else:
        form = ReviewForm()
        if request.user.is_authenticated:
            reviewed = Review.objects.all().filter(
                product=product).filter(user=user_profile.id)
        else:
            reviewed = False

        liked = False
        if product.likes.filter(id=request.user.id).exists():
            liked = True

        delivery = settings.STANDARD_DELIVERY

        context = {
            'product': product,
            'liked': liked,
            'form': form,
            'reviews': reviews,
            'review_count': review_count,
            'reviewed': reviewed,
            'delivery': delivery,
        }

        return render(request, 'products/product_detail.html', context)


def favourite_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.POST:
        if product.likes.filter(id=request.user.id).exists():
            product.likes.remove(request.user)
            messages.success(
                request, f'Removed {product.name} from your favourites'
                )
        else:
            product.likes.add(request.user)
            messages.success(
                request, f'Added {product.name} to your favourites'
                )
        return HttpResponseRedirect(
            reverse('product_detail', args=[product.id]))


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
                )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def feature_product(request, product_id):
    """ Toggles products feature status """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    redirect_url = request.POST.get('redirect_url')
    if request.POST:
        product = get_object_or_404(Product, pk=product_id)
        if product.featured:
            product.featured = False
            product.save()
            messages.success(request, 'Product unfeatured!')
        else:
            product.featured = True
            product.save()
            messages.success(request, 'Product Featured!')
        return redirect(redirect_url)
