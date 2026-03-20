from product import Product

class Category:
    def __init__(self, name: str):
        self.name = name
        self.__products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("В категорию можно добавлять только объекты Product и его наследников")
        self.__products.append(product)

    def get_products_info(self):
        """Возвращает список строк с информацией о товарах."""
        return [f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self.__products]

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

def add_product(self, product):
    if not isinstance(product, Product):
        raise TypeError("В категорию можно добавлять только объекты Product и его наследников")
    self.__products.append(product)