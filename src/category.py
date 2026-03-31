from src.product import Product

class ZeroQuantityError(Exception):
    pass

class Category:
    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("В категорию можно добавлять только объекты Product и его наследников")
        try:
            if product.quantity == 0:
                raise ZeroQuantityError("Попытка добавить товар с нулевым количеством")
            self.__products.append(product)
        except ZeroQuantityError as e:
            print(f"Ошибка: {e}")
        else:
            print("Товар добавлен")
        finally:
            print("Обработка добавления товара завершена")

    def get_products_info(self):
        return [f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self.__products]

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def middle_price(self):
        try:
            total = sum(p.price for p in self.__products)
            return total / len(self.__products)
        except ZeroDivisionError:
            return 0