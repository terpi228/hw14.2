import pytest
from unittest.mock import patch
from product import Product

def test_product_str():
    p = Product("Смартфон", 40000, 3)
    assert str(p) == "Смартфон, 40000 руб. Остаток: 3 шт."

def test_product_add():
    p1 = Product("Ноутбук", 80000, 2)
    p2 = Product("Мышь", 1500, 5)
    total_cost = p1 + p2
    expected = 80000 * 2 + 1500 * 5
    assert total_cost == expected

def test_product_add_wrong_type():
    p1 = Product("Книга", 500, 10)
    with pytest.raises(TypeError):
        p1 + "не товар"