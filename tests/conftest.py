import pytest

from src.oop_class_category import Category
from src.oop_class_product import Product


@pytest.fixture
def right_product():
    return Product("Samsung Galaxy S23 Ultra",
                   "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def right_cat():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, "
                    "но и получения дополнительных функций для удобства жизни",
                    [])


@pytest.fixture
def empty_cat():
    return Category(None, None, [])


@pytest.fixture
def empty_product():
    return Product("", "", 0.0, 0)


@pytest.fixture
def str_product():
    return Product(name="Product", description="Description of the product",
price=90.0, quanity=5,)


@pytest.fixture
def second_product():
    return Product(name="Product", description="Description of the product number two",
price=200.0, quanity=20,)


@pytest.fixture
def phone_1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

@pytest.fixture
def phone_2():
    return Product("Samsung Galaxy S24 Ultra", "256GB, Серый цвет, 200MP камера", 8000.0, 5)

@pytest.fixture
def firs_cat():
    return Category("Cмартфоны",
                         "Смартфоны, как средство не только коммуникации,"
                         " но и получения дополнительных функций для удобства жизни",
product=[Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
Product("Iphone 15", "512GB, Gray space", 210000.0, 8),],)