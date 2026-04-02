import pytest

from src.product import BaseProduct, LawnGrass, Product, Smartphone


def test_product_creation():
    """Создание продукта с корректными данными."""
    p = Product("Телефон", "Смартфон", 50000, 10)
    assert p.name == "Телефон"
    assert p.description == "Смартфон"
    assert p.price == 50000
    assert p.quantity == 10


def test_product_zero_quantity():
    """Попытка создать продукт с quantity = 0 вызывает ValueError."""
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Брак", "Описание", 100, 0)


def test_new_product_classmethod():
    """Классовый метод new_product создаёт продукт из словаря."""
    data = {"name": "Ноутбук", "description": "Игровой", "price": 70000, "quantity": 5}
    p = Product.new_product(data)
    assert p.name == "Ноутбук"
    assert p.description == "Игровой"
    assert p.price == 70000
    assert p.quantity == 5


def test_product_str():
    """Проверка строкового представления."""
    p = Product("Телефон", "Смартфон", 50000, 10)
    assert str(p) == "Телефон, 50000 руб. Остаток: 10 шт."


def test_product_add():
    """Сложение двух продуктов одного типа."""
    p1 = Product("Товар1", "Описание1", 100, 5)
    p2 = Product("Товар2", "Описание2", 200, 3)
    result = p1 + p2
    assert result == 100 * 5 + 200 * 3  # 500 + 600 = 1100


def test_product_add_wrong_type():
    """Сложение с объектом не Product вызывает TypeError."""
    p = Product("Товар", "Описание", 100, 5)
    with pytest.raises(TypeError, match="Можно складывать только объекты Product"):
        p + "строка"


def test_product_add_different_types():
    """Сложение продуктов разных классов вызывает TypeError."""
    p = Product("Обычный", "Описание", 100, 5)
    s = Smartphone("iPhone", "Описание", 120000, 1, "A16", "15", 128, "черный")
    with pytest.raises(TypeError, match="Нельзя складывать товары разных типов"):
        p + s


def test_price_getter():
    """Получение цены через property."""
    p = Product("Товар", "Описание", 1000, 2)
    assert p.price == 1000


def test_price_setter_positive():
    """Установка цены выше текущей (без запроса)."""
    p = Product("Товар", "Описание", 1000, 2)
    p.price = 1500
    assert p.price == 1500


def test_price_setter_zero_or_negative(capsys):
    """Установка цены <= 0 — печатается сообщение, цена не меняется."""
    p = Product("Товар", "Описание", 1000, 2)
    p.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert p.price == 1000

    p.price = -500
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert p.price == 1000


def test_price_setter_decrease_confirmed(monkeypatch, capsys):
    """Понижение цены с подтверждением."""
    p = Product("Товар", "Описание", 1000, 2)
    monkeypatch.setattr("builtins.input", lambda _: "y")
    p.price = 800
    captured = capsys.readouterr()
    assert "Цена товара 'Товар' обновлена до 800 руб." in captured.out
    assert p.price == 800


def test_price_setter_decrease_cancelled(monkeypatch, capsys):
    """Понижение цены с отказом."""
    p = Product("Товар", "Описание", 1000, 2)
    monkeypatch.setattr("builtins.input", lambda _: "n")
    p.price = 800
    captured = capsys.readouterr()
    assert "Изменение цены отменено" in captured.out
    assert p.price == 1000


def test_smartphone_creation():
    """Создание смартфона со всеми атрибутами."""
    s = Smartphone("iPhone", "Флагман", 120000, 1, "A16", "15", 128, "черный")
    assert s.name == "iPhone"
    assert s.description == "Флагман"
    assert s.price == 120000
    assert s.quantity == 1
    assert s.efficiency == "A16"
    assert s.model == "15"
    assert s.memory == 128
    assert s.color == "черный"


def test_lawn_grass_creation():
    """Создание газонной травы со всеми атрибутами."""
    lawn_grass = LawnGrass("Трава", "Семена", 1000, 10, "РФ", "10 дней", "зеленый")
    assert lawn_grass.name == "Трава"
    assert lawn_grass.description == "Семена"
    assert lawn_grass.price == 1000
    assert lawn_grass.quantity == 10
    assert lawn_grass.country == "РФ"
    assert lawn_grass.germination_period == "10 дней"
    assert lawn_grass.color == "зеленый"


def test_smartphone_str():
    """Строковое представление смартфона (наследуется от Product)."""
    s = Smartphone("iPhone", "Описание", 120000, 1, "A16", "15", 128, "черный")
    assert str(s) == "iPhone, 120000 руб. Остаток: 1 шт."


def test_lawn_grass_str():
    """Строковое представление травы."""
    item = LawnGrass("Трава", "Описание", 1000, 10, "РФ", "10 дней", "зеленый")
    assert str(item) == "Трава, 1000 руб. Остаток: 10 шт."


def test_inheritance():
    """Проверка, что дочерние классы являются экземплярами Product."""
    s = Smartphone("iPhone", "Описание", 120000, 1, "A16", "15", 128, "черный")
    i = LawnGrass("Трава", "Описание", 1000, 10, "РФ", "10 дней", "зеленый")
    assert isinstance(s, Product)
    assert isinstance(i, Product)


def test_log_mixin_output(capsys):
    """Проверка, что LogMixin выводит сообщение при создании."""
    # Сначала создай объект (он выведет сообщение)
    product = Product("Телефон", "Описание", 50000, 10)  # или класс с LogMixin

    # Теперь читаем вывод
    captured = capsys.readouterr()

    assert "Создан объект класса Product" in captured.out
    assert "Телефон" in captured.out
    assert "Описание" in captured.out
    assert "50000" in captured.out
    assert "10" in captured.out


def test_base_product_abstract():
    """Проверяем, что BaseProduct абстрактный (создать нельзя)."""
    with pytest.raises(TypeError):
        BaseProduct()
