from api.orders import place_order
from inventory.stock import STOCK


def test_place_order_reserves_stock():
    before = STOCK["sku1"]
    place_order([{"sku": "sku1", "price": 0, "qty": 2}])
    assert STOCK["sku1"] == before - 2
