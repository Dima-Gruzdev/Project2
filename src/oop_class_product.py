class Product:
    """Класс продукта с его общими свойствами и методам инициализации"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quanity):
        self.name = name if name else ""
        self.description = description if name else ""
        self.price = price if price else 0.0
        self.quantity = quanity if quanity else 0


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)
