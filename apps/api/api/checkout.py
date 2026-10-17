from payments.tax import calculate_tax
from payments.discounts import apply_discount
from api.shipping import shipping_cost


def calculate_order(cart, region="IN", code=None):
    subtotal = sum(item["price"] * item["qty"] for item in cart)
    subtotal = apply_discount(subtotal, code)
    return round(subtotal + calculate_tax(subtotal, region), 2)


def quote_with_shipping(cart, region="IN", code=None, distance_km=10):
    return calculate_order(cart, region, code) + shipping_cost(distance_km)
