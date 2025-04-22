from src.oop_class_product import Product


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


def test_new_product():
    dict_product = {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8}
    product = Product.new_product(dict_product)
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_str_prod(str_product):
    assert str(str_product) == "Product, 90.0 руб. Остаток:  5 шт."


def test_add_prod(phone_1, phone_2):
    assert phone_1 + phone_2 == 940000.0
