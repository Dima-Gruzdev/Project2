from src.oop_class_product import Product


class Category:
    name: str
    description: str
    product: str
    counter_categ = 0
    counter_produc = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.product = product
        Category.counter_categ += 1
        Category.counter_produc += len(product) if product else 0


if __name__ == "__main__":
    product = Product("Помидор", "Томат (или помидор) — "
                                 "однолетнее или многолетнее травянистое растение, "
                                 "вид рода Паслён (Solanum) семейства Паслёновые", 200, 100)
    product1 = Product("Жвачка", "кулинарное изделие, "
                                 "которое состоит из несъедобной эластичной основы "
                                 "и различных вкусовых и ароматических добавок.", 10, 500)
    category = Category("Овощи", "продукты", [product, product1])

    print(category.name)
    print(category.description)
    print(category.product)
    print(category.counter_categ)
    print(category.counter_produc)
