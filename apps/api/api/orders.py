from api.checkout import calculate_order
from inventory.stock import reserve


def place_order(cart, region="IN"):
    for item in cart:
        reserve(item["sku"], item["qty"])
    return calculate_order(cart, region)
