from src.base_product import BaseProduct
from src.print_mixin import MixinProduct


class Product(BaseProduct, MixinProduct):
    """Класс продукта с его общими свойствами и методам инициализации"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name if name else ""
        self.description = description if name else ""
        self.__price = price if price else 0.0
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен.")
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток:  {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            return self.quantity * self.price + other.quantity * other.price
        else:
            raise TypeError

    @classmethod
    def new_product(cls, new_product):
        name = new_product["name"]
        description = new_product["description"]
        price = new_product["price"]
        quantity = new_product["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, amount):
        if amount <= 0:
            print(f"Цена не может быть ниже или равна  0 как указали вы {amount}")
        else:
            self.__price = amount


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)
    print(product1 + product2)
