from src.lawngrass_product import LawnGrass
from src.oop_class_product import Product
from src.smartphone_product import Smartphone


def test_print_mixin(capsys):
    """ Тест на проверку правильности вывода в консоль """

    Product("Samsung Galaxy S23 Ultra",
            "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
               180000.0, 5, 1, "sams", 10, "red")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    LawnGrass("Samsung Galaxy S23 Ultra",
              "256GB, Серый цвет, 200MP камера", 180000.0,
              5, "China", "5 дней", "red")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
