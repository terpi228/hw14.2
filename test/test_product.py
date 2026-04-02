import pytest
from src.product import Product, Smartphone, LawnGrass

def test_product_init():
    p = Product("Телефон", 50000, 10)
    assert p.name == "Телефон"
    assert p.quantity == 10

def test_price_property():
    p = Product("Телефон", 50000, 10)
    assert p.price == 50000

def test_price_setter_up():
    p = Product("Телефон", 50000, 10)
    p.price = 60000
    assert p.price == 60000

def test_price_setter_negative():
    p = Product("Телефон", 50000, 10)
    p.price = -100
    assert p.price == 50000

def test_price_setter_decrease_yes(monkeypatch):
    p = Product("Телефон", 50000, 10)
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    p.price = 40000
    assert p.price == 40000

def test_price_setter_decrease_no(monkeypatch):
    p = Product("Телефон", 50000, 10)
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    p.price = 40000
    assert p.price == 50000

def test_str():
    p = Product("Телефон", 50000, 10)
    assert str(p) == "Телефон, 50000 руб. Остаток: 10 шт."

def test_add():
    p1 = Product("Телефон", 50000, 10)
    p2 = Product("Чехол", 1000, 30)
    assert p1 + p2 == 530000

def test_add_wrong_type():
    p = Product("Телефон", 50000, 10)
    with pytest.raises(TypeError):
        p + "string"

def test_add_different_types():
    p = Product("Телефон", 50000, 10)
    s = Smartphone("iPhone", 120000, 1, "A16", "15", 128, "черный")
    with pytest.raises(TypeError):
        p + s

def test_new_product():
    data = {'name': 'Телефон', 'price': 50000, 'quantity': 10}
    p = Product.new_product(data)
    assert p.name == "Телефон"

def test_smartphone():
    s = Smartphone("iPhone", 120000, 1, "A16", "15", 128, "черный")
    assert s.name == "iPhone"
    assert s.efficiency == "A16"

def test_lawn_grass():
    l = LawnGrass("Трава", 1000, 10, "РФ", "10 дней", "зеленый")
    assert l.name == "Трава"
    assert l.country == "РФ"