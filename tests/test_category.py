import pytest

from src.category import Category
from src.product import Product


def test_category_creation():
    """Создание категории увеличивает счётчик
    категорий и корректно инициализирует атрибуты"""
    cat = Category("Electronics", "Devices")
    assert cat.name == "Electronics"
    assert cat.description == "Devices"
    assert cat._Category__products == []
    assert Category.category_count == 1
    # Сбросим счётчики перед следующими тестами, если они влияют
    Category.category_count = 0
    Category.product_count = 0


def test_category_count_increments():
    """Каждый новый экземпляр Category увеличивает category_count"""
    Category.category_count = 0
    Category("A", "desc A")
    Category("B", "desc B")
    assert Category.category_count == 2
    Category.category_count = 0  # сброс


def test_add_product_valid():
    """Добавление продукта через add_product
    увеличивает product_count и сохраняет в __products"""
    Category.product_count = 0
    cat = Category("Cat", "Desc")
    prod = Product("Item", "Desc", 10.0, 3)
    cat.add_product(prod)
    assert len(cat._Category__products) == 1
    assert cat._Category__products[0] is prod
    assert Category.product_count == 1


def test_add_product_invalid_type():
    """Попытка добавить не-Product вызывает TypeError"""
    cat = Category("Cat", "Desc")
    with pytest.raises(TypeError, match="Добавить можно только объект класса Product"):
        cat.add_product("not a product")


def test_products_property():
    """Геттер products возвращает строковое представление товаров"""
    cat = Category("Cat", "Desc")
    p1 = Product("Phone", "Smart", 500.0, 2)
    p2 = Product("Laptop", "Gaming", 1500.0, 1)
    cat.add_product(p1)
    cat.add_product(p2)
    expected = "Phone, 500.0 руб. Остаток: 2 шт.\nLaptop, 1500.0 руб. Остаток: 1 шт.\n"
    assert cat.products == expected


def test_products_empty():
    """Если товаров нет, products возвращает пустую строку"""
    cat = Category("Empty", "Nothing")
    assert cat.products == ""


def test_category_initialization_with_products():
    """При создании категории с переданным списком продуктов они добавляются через add_product"""
    Category.product_count = 0
    p1 = Product("A", "a", 10, 1)
    p2 = Product("B", "b", 20, 2)
    cat = Category("Cat", "Desc", [p1, p2])
    assert len(cat._Category__products) == 2
    assert Category.product_count == 2
    # Проверяем содержимое
    assert cat._Category__products[0].name == "A"
    assert cat._Category__products[1].name == "B"
    Category.category_count = 0
    Category.product_count = 0
