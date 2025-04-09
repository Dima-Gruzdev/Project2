from itertools import product


class Product:
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quanity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quanity


if __name__ == "__main__":
    product = Product("Помидор", "Томат (или помидор) — "
                                 "однолетнее или многолетнее травянистое растение, "
                                 "вид рода Паслён (Solanum) семейства Паслёновые", 200, 100)
    print(product.name)
    print(product.description)
    print(f"{product.price} руб/кг")
    print(f"{product.quantity} кг")
