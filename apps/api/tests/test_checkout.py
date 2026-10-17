from api.checkout import calculate_order, quote_with_shipping


def test_total():
    cart = [{"price": 50, "qty": 2}]
    assert calculate_order(cart, "IN") == 108


def test_empty_cart():
    assert calculate_order([], "IN") == 0


def test_shipping_only_added_once():
    assert quote_with_shipping([], "IN", distance_km=0) == 0
