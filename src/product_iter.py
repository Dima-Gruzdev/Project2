from src.oop_class_category import Category
from src.oop_class_product import Product


class ProductIter:


    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.products):
            product = self.category.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


if __name__ == "__main":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации,"
                         " но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])
    iterator = ProductIter(category1)
    for prod in iterator:
        print(prod)


