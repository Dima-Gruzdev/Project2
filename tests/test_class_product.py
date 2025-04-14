
def test_product(right_product):
    assert right_product.name == "Samsung Galaxy S23 Ultra"
    assert right_product.description == "256GB, Серый цвет, 200MP камера"
    assert right_product.price == 180000.0
    assert right_product.quantity == 5


def test_empty_product(empty_product):
    assert empty_product.name == ""
    assert empty_product.description == ""
    assert empty_product.price == 0.0
    assert empty_product.quantity == 0
