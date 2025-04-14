from src.oop_class_category import Category


def test_cat(right_cat):
    assert right_cat.name == "Смартфоны"
    assert right_cat.description == ("Смартфоны, как средство не только коммуникации,"
                                     " но и получения дополнительных функций для удобства жизни")
    assert len(right_cat.product) == 0
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_empty_cat(empty_cat):
    assert empty_cat.name == ""
    assert empty_cat.description == ""
    assert empty_cat.product == []

    # assert Category.category_count == 1
    assert Category.product_count == 0
