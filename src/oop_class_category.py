from src.oop_class_product import Product


class Category:
    """Класс категории с его свойствами и методом инициализации """
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, product):
        self.name = name if name else ""
        self.description = description if description else ""
        self.__products = product if product else []
        Category.category_count += 1
        Category.product_count += len(product) if product else 0

    def __str__(self):
        total_qty = self.total_quantity()
        return f"{self.name}, количество продуктов: {total_qty} шт "


    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            print("product не является экземпляром класса Product")

    def total_quantity(self):
        return sum(product.quantity for product in self.__products)

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str


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
    print(category1.products)
    print(category1.category_count)
    print(category1.product_count)

    product5 = Product("Xiaomi Redmi Note 12", "1024GB, Синий", 55000.0, 10)
    category1.add_product(product5)
    print(category1.products)
    print(category1.product_count)
    print(category1)
