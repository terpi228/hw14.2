import pytest
from unittest.mock import patch
from product import Product

def test_product_creation():
    """Проверка создания товара через конструктор и класс-метод."""
    p1 = Product("Телефон", 50000, 10)
    assert p1.name == "Телефон"
    assert p1.price == 50000
    assert p1.quantity == 10

    p2 = Product.new_product({"name": "Чехол", "price": 1000, "quantity": 30})
    assert p2.name == "Чехол"
    assert p2.price == 1000
    assert p2.quantity == 30

def test_price_setter_positive():
    """Проверка установки корректной цены (повышение)."""
    p = Product("Ноутбук", 80000, 5)
    p.price = 85000   # повышение цены, подтверждение не нужно
    assert p.price == 85000

def test_price_setter_negative():
    """Проверка: установка цены <= 0 не меняет значение и выводит сообщение."""
    p = Product("Мышь", 1500, 20)
    p.price = -100
    assert p.price == 1500

def test_price_setter_zero():
    p = Product("Клавиатура", 2000, 10)
    p.price = 0
    assert p.price == 2000

def test_price_decrease_with_confirmation():
    """Проверка понижения цены с подтверждением."""
    p = Product("Монитор", 25000, 3)
    with patch('builtins.input', return_value='y'):
        p.price = 23000
    assert p.price == 23000

def test_price_decrease_cancelled():
    """Проверка отмены понижения цены."""
    p = Product("Монитор", 25000, 3)
    with patch('builtins.input', return_value='n'):
        p.price = 23000
    assert p.price == 25000   # цена не изменилась

def test_price_increase_no_confirmation():
    """Повышение цены не требует подтверждения."""
    p = Product("Смартфон", 40000, 7)
    p.price = 45000
    assert p.price == 45000