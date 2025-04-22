from src.oop_class_product import Product


class Smartphone(Product):
    """ подкласс для родительского класса Product для добавление категорий """
    def __init__(self, name: str, description: str,
                 price: float, quanity: int, efficiency: float, model: str, memory: int, color: str):
        """Метод инициализация категорий"""
        super().__init__(name, description, price, quanity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """ метод сложения из одинаковых классов продуктов """
        if type(other) is Smartphone:
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError


if __name__ == "__main__":
    smart_product = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                               180000.0, 5, 1, "sams", 10, "red")
    print(smart_product.efficiency)
    print(smart_product.color)
    print(smart_product.memory)
    print(smart_product.model)
