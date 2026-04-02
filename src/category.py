from src.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = []  # Приватный атрибут
        if products:
            for product in products:
                self.add_product(product)

        Category.category_count += 1

    def add_product(self, product: Product):
        """Метод для добавления продукта в список товаров категории"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Добавить можно только объект класса Product")

    @property
    def products(self) -> str:
        """Геттер возвращает список товаров в строковом представлении"""
        result = ""
        for product in self.__products:
            result += (
                f"{product.name},"
                f" {product.price} руб. Остаток:"
                f" {product.quantity} шт.\n"
            )
        return result


if __name__ == "__main__":
    # Тестовые данные
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации",
        [product1, product2, product3],
    )
    # Проверка геттера списка товаров
    print("Список товаров в категории:")
    print(category1.products)
    # Проверка добавления нового товара
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print("После добавления нового товара:")
    print(category1.products)
    # Проверка создания через factory-method
    new_prod_data = {
        "name": "Nokia 3310",
        "description": "Легенда",
        "price": 5000.0,
        "quantity": 10,
    }
    product5 = Product.new_product(new_prod_data)
    category1.add_product(product5)
    # Проверка логики изменения цены
    print(f"Текущая цена {product5.name}: {product5.price}")

    # Попытка установить некорректную цену
    product5.price = -10

    # Попытка снижения цены (с инпутом)
    product5.price = 4500.0
    print(f"Итоговая цена {product5.name}: {product5.price}")
