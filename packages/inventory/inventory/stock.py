STOCK = {"sku1": 10, "sku2": 5}


def reserve(sku, qty):
    if STOCK.get(sku, 0) < qty:
        raise ValueError("insufficient stock")
    STOCK[sku] -= qty
