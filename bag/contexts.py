from decimal import Decimal

from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from checkout.models import Order
from coupons.models import Coupon
from profiles.models import UserProfile
from coupons.forms import CouponApplyForm


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    # Checks if user has ordered before
    user_has_orders = False

    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        orders = Order.objects.all().filter(user_profile=profile)
        if len(orders) >= 1:
            user_has_orders = True

    # Works out delivery total
    if request.user.is_authenticated and user_has_orders is False:
        delivery = 0
        free_delivery_delta = 0
    elif total != 0 and total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = product_count * (settings.STANDARD_DELIVERY)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    # Reworks total if coupon has been used
    coupon_apply_form = CouponApplyForm()
    coupon_id = request.session.get('coupon_id')
    before_coupon = 0
    if coupon_id:
        before_coupon = total
        coupon = Coupon.objects.get(id=coupon_id)
        discount_as_decimal = Decimal(coupon.discount / 100)
        discount = total * discount_as_decimal
        total = total - discount
    else:
        coupon = ''
        discount = 0

    pre_delivery = product_count * settings.STANDARD_DELIVERY
    grand_total = delivery + total
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'user_has_orders': user_has_orders,
        'pre_delivery': pre_delivery,
        'coupon_apply_form': coupon_apply_form,
        'coupon': coupon,
        'before_coupon': before_coupon,
        'discount': discount,
    }

    return context
