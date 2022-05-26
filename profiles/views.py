from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order
from products.models import Product


@login_required
def profile(request):
    """ Display the user's profile """

    profile = get_object_or_404(UserProfile, user=request.user)
    products = Product.objects.filter(likes=request.user.id)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Information updated successfully')
        else:
            messages.error(
                request,
                'Update failed. Please check your information and try again.'
                )
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
        'products': products,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ Displays the user's previous orders """
    order = get_object_or_404(Order, order_number=order_number)
    order_date = order.date.strftime("%d-%m-%Y %H:%M:%S")

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        f'A confirmation email was sent on { order_date }.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
