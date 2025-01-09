from django import template
from App_Order.models import Order


register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].orderitems.count()
    return 0