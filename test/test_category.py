import pytest
from src.product import Product, Smartphone, LawnGrass
from src.category import Category

def test_init():
    cat = Category("Электроника")
    assert cat.name == "Электроника"
    assert cat._Category__products == []

def test_add_product():
    cat = Category("Электроника")
    p = Product("Телефон", 50000, 10)
    cat.add_product(p)
    assert len(cat._Category__products) == 1
    assert cat._Category__products[0] == p

def test_add_product_wrong_type():
    cat = Category("Тест")
    with pytest.raises(TypeError):
        cat.add_product("не товар")

def test_add_product_inherited():
    cat = Category("Тест")
    s = Smartphone("iPhone", 120000, 1, "A16", "15", 128, "черный")
    cat.add_product(s)
    assert len(cat._Category__products) == 1
    assert isinstance(cat._Category__products[0], Smartphone)

def test_get_products_info():
    cat = Category("Тест")
    cat.add_product(Product("Телефон", 50000, 10))
    info = cat.get_products_info()
    assert info == ["Телефон, 50000 руб. Остаток: 10 шт."]

def test_get_products_info_empty():
    cat = Category("Тест")
    assert cat.get_products_info() == []

def test_str():
    cat = Category("Тест")
    cat.add_product(Product("Товар", 100, 5))
    cat.add_product(Product("Товар2", 200, 3))
    assert str(cat) == "Тест, количество продуктов: 8 шт."

def test_str_empty():
    cat = Category("Тест")
    assert str(cat) == "Тест, количество продуктов: 0 шт."

def test_str_with_inherited():
    cat = Category("Смешанная")
    cat.add_product(Product("Обычный", 100, 5))
    cat.add_product(Smartphone("Смартфон", 50000, 2, "A16", "15", 128, "черный"))
    cat.add_product(LawnGrass("Трава", 1000, 3, "РФ", "10 дней", "зеленый"))
    assert str(cat) == "Смешанная, количество продуктов: 10 шт."

def test_multiple_adds():
    cat = Category("Тест")
    for i in range(3):
        cat.add_product(Product(f"Товар{i}", 100, 1))
    assert len(cat._Category__products) == 3

def test_dunder_methods():
    cat = Category("Тест")
    pass

def test_add_product_multiple_wrong_types():
    cat = Category("Тест")
    with pytest.raises(TypeError):
        cat.add_product([])
    with pytest.raises(TypeError):
        cat.add_product({})
    with pytest.raises(TypeError):
        cat.add_product(None)