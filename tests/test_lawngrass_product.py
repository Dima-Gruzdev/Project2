def test_lawngrass(lawngrass_prod):
    """Тест для проверки  корректного возращения данных"""
    assert lawngrass_prod.name == "Samsung Galaxy S23 Ultra"
    assert lawngrass_prod.description == "256GB, Серый цвет, 200MP камера"
    assert lawngrass_prod.price == 180000.0
    assert lawngrass_prod.quantity == 5
    assert lawngrass_prod.country == "China"
    assert lawngrass_prod.germination_period == "5 дней"
    assert lawngrass_prod.color == "red"


def test_lawngrass_sum(lawngrass_prod, lawngrass_prod2):
    """ Тест для проверки сложения """
    assert lawngrass_prod + lawngrass_prod2 == 1000000.0
