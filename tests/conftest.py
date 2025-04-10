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
