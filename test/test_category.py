import pytest
from src.product import Product, Smartphone, LawnGrass
from src.category import Category

def test_init():
    cat = Category("Электроника", "Описание", [])
    assert cat.name == "Электроника"
    assert cat._Category__products == []

def test_add_product():
    cat = Category("Электроника", "Описание", [])
    p = Product("Телефон", "описание", 50000, 10)
    cat.add_product(p)
    assert len(cat._Category__products) == 1
    assert cat._Category__products[0] == p

def test_add_product_wrong_type():
    cat = Category("Тест", "Описание", [])
    with pytest.raises(TypeError):
        cat.add_product("не товар")

def test_add_product_inherited():
    cat = Category("Тест", "Описание", [])
    s = Smartphone("iPhone", "описание", 120000, 1, "A16", "15", 128, "черный")
    cat.add_product(s)
    assert len(cat._Category__products) == 1
    assert isinstance(cat._Category__products[0], Smartphone)

def test_get_products_info():
    cat = Category("Тест", "Описание", [])
    cat.add_product(Product("Телефон", "описание", 50000, 10))
    info = cat.get_products_info()
    assert info == ["Телефон, 50000 руб. Остаток: 10 шт."]

def test_get_products_info_empty():
    cat = Category("Тест", "Описание", [])
    assert cat.get_products_info() == []

def test_str():
    cat = Category("Тест", "Описание", [])
    cat.add_product(Product("Товар", "описание", 100, 5))
    cat.add_product(Product("Товар2", "описание", 200, 3))
    assert str(cat) == "Тест, количество продуктов: 8 шт."

def test_str_empty():
    cat = Category("Тест", "Описание", [])
    assert str(cat) == "Тест, количество продуктов: 0 шт."

def test_str_with_inherited():
    cat = Category("Смешанная", "Описание", [])
    cat.add_product(Product("Обычный", "описание", 100, 5))
    cat.add_product(Smartphone("Смартфон", "описание", 50000, 2, "A16", "15", 128, "черный"))
    cat.add_product(LawnGrass("Трава", "описание", 1000, 3, "РФ", "10 дней", "зеленый"))
    assert str(cat) == "Смешанная, количество продуктов: 10 шт."

def test_multiple_adds():
    cat = Category("Тест", "Описание", [])
    for i in range(3):
        cat.add_product(Product(f"Товар{i}", "описание", 100, 1))
    assert len(cat._Category__products) == 3

def test_dunder_methods():
    cat = Category("Тест", "Описание", [])
    pass

def test_add_product_multiple_wrong_types():
    cat = Category("Тест", "Описание", [])
    with pytest.raises(TypeError):
        cat.add_product([])
    with pytest.raises(TypeError):
        cat.add_product({})
    with pytest.raises(TypeError):
        cat.add_product(None)

# Новые тесты для задания 17.1
def test_middle_price():
    cat = Category("Тест", "Описание", [])
    cat.add_product(Product("Товар1", "описание", 100, 5))
    cat.add_product(Product("Товар2", "описание", 200, 3))
    assert cat.middle_price() == 150.0

def test_middle_price_empty():
    cat = Category("Пусто", "Описание", [])
    assert cat.middle_price() == 0