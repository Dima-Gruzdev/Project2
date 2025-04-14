from src.oop_class_product import Product


class Category:
    """Класс категории с его свойствами и методом инициализации """
    name: str
    description: str
    product: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, product):
        self.name = name if name else ""
        self.description = description if description else ""
        self.product = product if product else []
        Category.category_count += 1
        Category.product_count += len(product) if product else 0


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации,"
                         " но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])
    print(category1.name)
    print(category1.description)
    print(category1.product)
    print(category1.category_count)
    print(category1.product_count)
