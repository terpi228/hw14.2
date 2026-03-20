import pytest
from product import Product
from category import Category

def test_add_product():
    cat = Category("Электроника")
    p1 = Product("Телефон", 50000, 10)
    p2 = Product("Чехол", 1000, 30)

    cat.add_product(p1)
    cat.add_product(p2)

    info = cat.get_products_info()
    assert len(info) == 2
    assert "Телефон, 50000 руб. Остаток: 10 шт." in info
    assert "Чехол, 1000 руб. Остаток: 30 шт." in info

def test_get_products_info_empty():
    cat = Category("Пустая")
    assert cat.get_products_info() == []

def test_private_products_attribute():
    """Проверка, что список товаров приватный."""
    cat = Category("Тест")
    assert hasattr(cat, "_Category__products")