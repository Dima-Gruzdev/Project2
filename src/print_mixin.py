class MixinProduct:
    def __init__(self):
        """ Метод инициализации """

        print(repr(self))

    def __repr__(self):
        """Метод вывода в консоль информации от какого класса вывод"""

        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
