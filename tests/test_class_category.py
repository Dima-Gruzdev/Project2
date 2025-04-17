from src.oop_class_category import Category


def test_cat(right_cat):
    assert right_cat.name == "Смартфоны"
    assert right_cat.description == ("Смартфоны, как средство не только коммуникации,"
                                     " но и получения дополнительных функций для удобства жизни")


def test_empty_cat(empty_cat):
    assert empty_cat.name == ""
    assert empty_cat.description == ""
    assert empty_cat.products == ""
    assert Category.product_count == 0


def test_str_cat(firs_cat):
    assert str(firs_cat) =='Cмартфоны, количество продуктов: 2 шт '