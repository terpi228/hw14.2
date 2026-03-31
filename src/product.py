from abc import ABC, abstractmethod

# Абстрактный базовый класс
class BaseProduct(ABC):
    @abstractmethod
    def __str__(self):
        """Строковое представление товара."""
        pass

    @abstractmethod
    def __add__(self, other):
        """Сложение товаров (стоимость)."""
        pass

    @property
    @abstractmethod
    def price(self):
        """Геттер цены."""
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        """Сеттер цены."""
        pass


# Миксин для логирования
class LogMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   # вызываем следующий __init__ по цепочке
        # Формируем строку с параметрами
        params = ", ".join(repr(arg) for arg in args)
        if kwargs:
            params += ", " + ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        print(f"Создан объект класса {self.__class__.__name__}({params})")


# Теперь Product наследует от миксина и абстрактного класса
class Product(LogMixin, BaseProduct):
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.__price = price
        self.quantity = quantity
        # Вызываем super().__init__ для передачи управления миксину
        super().__init__(name, price, quantity)

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data['name'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    def __str__(self):
        """Строковое представление товара."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных типов")
        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            answer = input(f"Вы действительно хотите понизить цену с {self.__price} до {new_price}? (y/n): ").strip().lower()
            if answer != 'y':
                print("Изменение цены отменено")
                return
        self.__price = new_price
        print(f"Цена товара '{self.name}' обновлена до {new_price} руб.")


class Smartphone(Product):
    def __init__(self, name: str, price: float, quantity: int, efficiency: str, model: str, memory: int, color: str):
        super().__init__(name, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, price, quantity, country, germination_period, color):
        super().__init__(name, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color