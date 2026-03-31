import pytest
from src.product import Product, Smartphone, LawnGrass
from src.category import Category

def test_init():
    cat = Category("Электроника", "Описание", [])
    assert cat.name == "Электроника"
    assert cat.description == "Описание"
    assert cat.products == []
    assert Category.category_count == 1
    # сбросим счетчики для чистоты тестов (в реальных тестах лучше использовать фикстуры)
    Category.category_count = 0
    Category.product_count = 0

def test_add_product():
    cat = Category("Электроника", "Описание", [])
    p = Product("Телефон", "описание", 50000, 10)
    cat.add_product(p)
    assert len(cat.products) == 1
    assert cat.products[0] == p
    assert Category.product_count == 1
    Category.category_count = 0
    Category.product_count = 0

def test_add_product_wrong_type():
    cat = Category("Тест", "Описание", [])
    with pytest.raises(TypeError):
        cat.add_product("не товар")
    Category.category_count = 0
    Category.product_count = 0

def test_add_product_inherited():
    cat = Category("Тест", "Описание", [])
    s = Smartphone("iPhone", "описание", 120000, 1, "A16", "15", 128, "черный")
    cat.add_product(s)
    assert len(cat.products) == 1
    assert isinstance(cat.products[0], Smartphone)
    Category.category_count = 0
    Category.product_count = 0

def test_get_products_info():
    cat = Category("Тест", "Описание", [])
    cat.add_product(Product("Телефон", "описание", 50000, 10))
    info = cat.get_products_info()
    assert info == ["Телефон, 50000 руб. Остаток: 10 шт."]
    Category.category_count = 0
    Category.product_count = 0

def test_get_products_info_empty():
    cat = Category("Тест", "Описание", [])
    assert cat.get_products_info() == []
    Category.category_count = 0
    Category.product_count = 0

def test_str():
    cat = Category("Тест", "Описание", [])
    cat.add_product(Product("Товар", "описание", 100, 5))
    cat.add_product(Product("Товар2", "описание", 200, 3))
    assert str(cat) == "Тест, количество продуктов: 8 шт."
    Category.category_count = 0
    Category.product_count = 0

def test_str_empty():
    cat = Category("Тест", "Описание", [])
    assert str(cat) == "Тест, количество продуктов: 0 шт."
    Category.category_count = 0
    Category.product_count = 0

def test_str_with_inherited():
    cat = Category("Смешанная", "Описание", [])
    cat.add_product(Product("Обычный", "описание", 100, 5))
    cat.add_product(Smartphone("Смартфон", "описание", 50000, 2, "A16", "15", 128, "черный"))
    cat.add_product(LawnGrass("Трава", "описание", 1000, 3, "РФ", "10 дней", "зеленый"))
    assert str(cat) == "Смешанная, количество продуктов: 10 шт."
    Category.category_count = 0
    Category.product_count = 0

def test_multiple_adds():
    cat = Category("Тест", "Описание", [])
    for i in range(3):
        cat.add_product(Product(f"Товар{i}", "описание", 100, 1))
    assert len(cat.products) == 3
    Category.category_count = 0
    Category.product_count = 0

def test_category_count():
    Category.category_count = 0
    Category.product_count = 0
    cat1 = Category("Кат1", "Описание", [])
    cat2 = Category("Кат2", "Описание", [])
    assert Category.category_count == 2
    # сброс
    Category.category_count = 0
    Category.product_count = 0

def test_product_count():
    Category.category_count = 0
    Category.product_count = 0
    cat = Category("Кат", "Описание", [])
    cat.add_product(Product("Товар1", "описание", 100, 5))
    cat.add_product(Product("Товар2", "описание", 200, 3))
    assert Category.product_count == 2
    Category.category_count = 0
    Category.product_count = 0

def test_dunder_methods():
    pass

def test_add_product_multiple_wrong_types():
    cat = Category("Тест", "Описание", [])
    with pytest.raises(TypeError):
        cat.add_product([])
    with pytest.raises(TypeError):
        cat.add_product({})
    with pytest.raises(TypeError):
        cat.add_product(None)
    Category.category_count = 0
    Category.product_count = 0