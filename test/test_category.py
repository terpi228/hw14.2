import pytest

from src.category import Category
from src.product import Product, Smartphone


def test_category_init_without_products():
    """Создание категории без списка продуктов."""
    cat = Category("Электроника", "Бытовая техника")
    assert cat.name == "Электроника"
    assert cat.description == "Бытовая техника"
    assert cat._Category__products == []


def test_category_init_with_products():
    """Создание категории с начальным списком продуктов."""
    p1 = Product("Телефон", "Смартфон", 50000, 10)
    p2 = Product("Чехол", "Аксессуар", 1000, 30)
    cat = Category("Аксессуары", "Разное", [p1, p2])
    assert cat.name == "Аксессуары"
    assert cat.description == "Разное"
    assert cat._Category__products == [p1, p2]


def test_add_product_success(capsys):
    """Добавление продукта с ненулевым количеством."""
    cat = Category("Тест", "Описание")
    p = Product("Товар", "Описание", 100, 5)
    cat.add_product(p)
    captured = capsys.readouterr()
    assert "Товар добавлен" in captured.out
    assert "Обработка добавления товара завершена" in captured.out
    assert cat._Category__products == [p]


def test_add_product_zero_quantity(capsys):
    """Добавление продукта с quantity == 0 вызывает исключение ZeroQuantityError и не добавляет."""
    cat = Category("Тест", "Описание")
    # Создаём продукт с ненулевым количеством, потом подменяем поле quantity,
    # потому что конструктор не позволяет создать с 0.
    p = Product("Брак", "Описание", 100, 5)
    p.quantity = 0
    cat.add_product(p)
    captured = capsys.readouterr()
    assert "Ошибка: Попытка добавить товар с нулевым количеством" in captured.out
    assert "Обработка добавления товара завершена" in captured.out
    assert "Товар добавлен" not in captured.out
    assert cat._Category__products == []


def test_add_product_wrong_type():
    """Попытка добавить не-продукт вызывает TypeError."""
    cat = Category("Тест", "Описание")
    with pytest.raises(
        TypeError,
        match="В категорию можно добавлять только объекты Product и его наследников",
    ):
        cat.add_product("строка")
    with pytest.raises(TypeError):
        cat.add_product(123)


def test_add_product_inherited():
    """Добавление наследника Product (Smartphone)."""
    cat = Category("Тест", "Описание")
    s = Smartphone("iPhone", "Флагман", 120000, 1, "A16", "15", 128, "черный")
    cat.add_product(s)
    assert cat._Category__products == [s]


def test_get_products_info():
    """Получение информации о товарах в категории."""
    cat = Category("Тест", "Описание")
    cat.add_product(Product("Телефон", "Смартфон", 50000, 10))
    cat.add_product(Product("Чехол", "Аксессуар", 1000, 30))
    info = cat.get_products_info()
    expected = [
        "Телефон, 50000 руб. Остаток: 10 шт.",
        "Чехол, 1000 руб. Остаток: 30 шт.",
    ]
    assert info == expected


def test_get_products_info_empty():
    """Пустая категория возвращает пустой список."""
    cat = Category("Пусто", "Описание")
    assert cat.get_products_info() == []


def test_str_nonempty():
    """Строковое представление непустой категории."""
    cat = Category("Тест", "Описание")
    cat.add_product(Product("Товар1", "Описание1", 100, 5))
    cat.add_product(Product("Товар2", "Описание2", 200, 3))
    assert str(cat) == "Тест, количество продуктов: 8 шт."


def test_str_empty():
    """Строковое представление пустой категории."""
    cat = Category("Пусто", "Описание")
    assert str(cat) == "Пусто, количество продуктов: 0 шт."


def test_middle_price_with_products():
    """Средняя цена при наличии продуктов."""
    cat = Category("Тест", "Описание")
    cat.add_product(Product("Товар1", "Описание1", 100, 5))
    cat.add_product(Product("Товар2", "Описание2", 200, 3))
    assert cat.middle_price() == 150.0  # (100+200)/2


def test_middle_price_empty():
    """Средняя цена для пустой категории — 0."""
    cat = Category("Пусто", "Описание")
    assert cat.middle_price() == 0
