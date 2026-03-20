from product import Product

class Category:
    def __init__(self, name: str):
        self.name = name
        self.__products = []

    def add_product(self, product: Product):
        """Добавляет товар в категорию."""
        self.__products.append(product)

    def get_products_info(self):
        """Возвращает список строк с информацией о товарах."""
        return [f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self.__products]
