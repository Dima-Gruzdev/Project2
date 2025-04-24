

def test_smart_prod(smart_prod):
    """ Тест что возращает все верные значения """
    assert smart_prod.name == "Samsung Galaxy S23 Ultra"
    assert smart_prod.description == "256GB, Серый цвет, 200MP камера"
    assert smart_prod.price == 180000.0
    assert smart_prod.quantity == 5
    assert smart_prod.efficiency == 1
    assert smart_prod.model == "sams"
    assert smart_prod.memory == 10
    assert smart_prod.color == "red"


def test_smart_prod_empty(empty_smart):
    """ Тест что возращает пустой строки или 0 при отсутсвии данных """
    assert empty_smart.name == ""
    assert empty_smart.description == ""
    assert empty_smart.price == 0.0
    assert empty_smart.quantity == 0
    assert empty_smart.efficiency == 0
    assert empty_smart.model == ""
    assert empty_smart.memory == 0
    assert empty_smart.color == ""


def test_smart_sum(smart_prod, smart_prod2):
    """ Тест сложения """
    assert smart_prod + smart_prod2 == 1150000.0
