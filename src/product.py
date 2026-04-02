class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict, current_products: list = None):
        """
        Создает объект Product из словаря.
        Дополнительно: проверяет наличие дубликата в списке current_products.
        """
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")
        if current_products:
            for existing_product in current_products:
                if existing_product.name == name:
                    # Складываем количество
                    existing_product.quantity += quantity
                    # Выбираем максимальную цену
                    existing_product.price = max(existing_product.price, price)
                    return existing_product
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        # Дополнительное задание: подтверждение снижения цены
        if new_price < self.__price:
            user_answer = input(
                f"Цена товара {self.name} снижается. Вы уверены? (y/n): "
            ).lower()
            if user_answer != "y":
                print("Изменение цены отменено.")
                return
        self.__price = new_price
