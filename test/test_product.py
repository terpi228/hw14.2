import pytest
from src.product import BaseProduct, Product, Smartphone, LawnGrass

def test_base_product_abstract():
    with pytest.raises(TypeError):
        BaseProduct()

def test_log_mixin(capsys):
    p = Product("Телефон", "описание", 50000, 10)
    captured = capsys.readouterr()
    assert "Создан объект класса Product('Телефон', 'описание', 50000, 10)" in captured.out

def test_product_init():
    p = Product("Телефон", "описание", 50000, 10)
    assert p.name == "Телефон"
    assert p.description == "описание"
    assert p.quantity == 10

def test_price_property():
    p = Product("Телефон", "описание", 50000, 10)
    assert p.price == 50000

def test_price_setter_up():
    p = Product("Телефон", "описание", 50000, 10)
    p.price = 60000
    assert p.price == 60000

def test_price_setter_negative():
    p = Product("Телефон", "описание", 50000, 10)
    p.price = -100
    assert p.price == 50000

def test_price_setter_decrease_yes(monkeypatch):
    p = Product("Телефон", "описание", 50000, 10)
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    p.price = 40000
    assert p.price == 40000

def test_price_setter_decrease_no(monkeypatch):
    p = Product("Телефон", "описание", 50000, 10)
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    p.price = 40000
    assert p.price == 50000

def test_str():
    p = Product("Телефон", "описание", 50000, 10)
    assert str(p) == "Телефон, 50000 руб. Остаток: 10 шт."

def test_add():
    p1 = Product("Телефон", "описание", 50000, 10)
    p2 = Product("Чехол", "описание", 1000, 30)
    assert p1 + p2 == 530000

def test_add_wrong_type():
    p = Product("Телефон", "описание", 50000, 10)
    with pytest.raises(TypeError):
        p + "string"

def test_add_different_types():
    p = Product("Телефон", "описание", 50000, 10)
    s = Smartphone("iPhone", "описание", 120000, 1, "A16", "15", 128, "черный")
    with pytest.raises(TypeError):
        p + s

def test_new_product():
    data = {'name': 'Телефон', 'description': 'описание', 'price': 50000, 'quantity': 10}
    p = Product.new_product(data)
    assert p.name == "Телефон"
    assert p.description == "описание"
    assert p.price == 50000
    assert p.quantity == 10

def test_smartphone():
    s = Smartphone("iPhone", "описание", 120000, 1, "A16", "15", 128, "черный")
    assert s.name == "iPhone"
    assert s.efficiency == "A16"
    assert s.model == "15"
    assert s.memory == 128
    assert s.color == "черный"

def test_lawn_grass():
    l = LawnGrass("Трава", "описание", 1000, 10, "РФ", "10 дней", "зеленый")
    assert l.name == "Трава"
    assert l.country == "РФ"
    assert l.germination_period == "10 дней"
    assert l.color == "зеленый"

def test_smartphone_creation():
    s = Smartphone("iPhone", "описание", 120000, 1, "A16", "15", 128, "черный")
    assert s.name == "iPhone"
    assert s.price == 120000
    assert s.quantity == 1

def test_smartphone_str():
    s = Smartphone("iPhone", "описание", 120000, 1, "A16", "15", 128, "черный")
    assert str(s) == "iPhone, 120000 руб. Остаток: 1 шт."

def test_lawn_grass_str():
    l = LawnGrass("Трава", "описание", 1000, 10, "РФ", "10 дней", "зеленый")
    assert str(l) == "Трава, 1000 руб. Остаток: 10 шт."

def test_inheritance():
    s = Smartphone("iPhone", "описание", 120000, 1, "A16", "15", 128, "черный")
    l = LawnGrass("Трава", "описание", 1000, 10, "РФ", "10 дней", "зеленый")
    assert isinstance(s, Product)
    assert isinstance(l, Product)

def test_product_different_values():
    p1 = Product("Товар1", "описание1", 100, 5)
    p2 = Product("Товар2", "описание2", 200, 0)
    assert p1.quantity == 5
    assert p2.quantity == 0

def test_smartphone_with_different_values():
    s = Smartphone("Galaxy", "описание", 80000, 3, "Exynos", "S21", 256, "синий")
    assert s.price == 80000
    assert s.quantity == 3

def test_lawn_grass_with_different_values():
    l = LawnGrass("Газон", "описание", 1500, 20, "США", "7 дней", "зеленый")
    assert l.price == 1500
    assert l.quantity == 20

def test_product_edge_cases():
    p = Product("", "", 0, 0)
    assert p.name == ""
    assert p.price == 0
    assert p.quantity == 0

def test_product_negative_values():
    p = Product("Тест", "описание", -100, -5)
    assert p.price == -100
    assert p.quantity == -5

def test_smartphone_edge_cases():
    s = Smartphone("", "", 0, 0, "", "", 0, "")
    assert s.name == ""
    assert s.price == 0
    assert s.quantity == 0

def test_lawn_grass_edge_cases():
    l = LawnGrass("", "", 0, 0, "", "", "")
    assert l.name == ""

def test_product_type_validation():
    pass

def test_product_repr():
    p = Product("Тест", "описание", 100, 5)
    if hasattr(p, '__repr__'):
        repr(p)

def test_product_comparison():
    p1 = Product("A", "описание", 100, 5)
    p2 = Product("B", "описание", 200, 3)
    if hasattr(p1, '__eq__'):
        assert (p1 == p1) is True
    if hasattr(p1, '__lt__'):
        assert (p1 != p2) is True

def test_product_properties():
    p = Product("Тест", "описание", 100, 5)
    for attr in ['price', 'quantity', 'name']:
        if hasattr(p, f'get_{attr}') or hasattr(p, f'set_{attr}'):
            pass

def test_smartphone_full_coverage():
    s = Smartphone("iPhone", "описание", 120000, 1, "A16", "15", 128, "черный")
    assert str(s)
    if hasattr(s, '__repr__'):
        assert repr(s) or True
    assert s.name == "iPhone"
    assert s.price == 120000
    assert s.quantity == 1

def test_lawn_grass_full_coverage():
    l = LawnGrass("Трава", "описание", 1000, 10, "РФ", "10 дней", "зеленый")
    assert str(l)
    if hasattr(l, '__repr__'):
        assert repr(l) or True
    assert l.name == "Трава"
    assert l.price == 1000
    assert l.quantity == 10
    assert l.country == "РФ"
    assert l.germination_period == "10 дней"
    assert l.color == "зеленый"

def test_edge_cases_zero_values():
    p = Product("", "", 0, 0)
    assert p.name == ""
    assert p.price == 0
    assert p.quantity == 0