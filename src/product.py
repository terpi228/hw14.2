from abc import ABC, abstractmethod

class BaseProduct(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        pass


class LogMixin:
    def __init__(self, *args, **kwargs):
        self._log_args = args
        self._log_kwargs = kwargs
        super().__init__()
        params = ", ".join(repr(arg) for arg in args)
        if kwargs:
            params += ", " + ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        print(f"Создан объект класса {self.__class__.__name__}({params})")


class Product(LogMixin, BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__(name, description, price, quantity)  # передаем в миксин

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data['name'],
            description=product_data.get('description', ''),
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    def __str__(self):
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
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: str, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color