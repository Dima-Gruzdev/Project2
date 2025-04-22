from src.oop_class_product import Product


class LawnGrass(Product):
    """ подкласс для родительского класса Product для добавление свойств """

    def __init__(self, name, description, price,
                 quanity, country, germination_period, color):
        """ Метод инициализации категории """
        super().__init__(name, description, price, quanity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """ метод сложения из одинаковых классов продуктов """
        if type(other) is LawnGrass:
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError


if __name__ == "__main":
    lawn_grass_prod = LawnGrass("Samsung Galaxy S23 Ultra",
                                "256GB, Серый цвет, 200MP камера", 180000.0,
                                5, "China", 3, "red")
    print(lawn_grass_prod.color)
    print(lawn_grass_prod.germination_period)
    print(lawn_grass_prod.country)
