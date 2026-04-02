from src.product import Product


def test_product_creation():
    """Тест создания продукта и работы геттера цены"""
    product = Product("Test", "Desc", 100.0, 5)
    assert product.name == "Test"
    assert product.description == "Desc"
    assert product.price == 100.0
    assert product.quantity == 5


def test_price_setter_negative(monkeypatch, capsys):
    """Попытка установить отрицательную цену – цена не меняется, печатается ошибка"""
    product = Product("Test", "Desc", 100.0, 5)
    product.price = -50
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100.0


def test_price_setter_zero(monkeypatch, capsys):
    """Попытка установить нулевую цену – цена не меняется"""
    product = Product("Test", "Desc", 100.0, 5)
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100.0


def test_price_setter_decrease_confirmed(monkeypatch):
    """Снижение цены с подтверждением 'y' – цена меняется"""
    product = Product("Test", "Desc", 100.0, 5)
    # Имитируем ввод 'y'
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 80.0
    assert product.price == 80.0


def test_price_setter_decrease_cancelled(monkeypatch, capsys):
    """Снижение цены с отказом – цена остаётся прежней"""
    product = Product("Test", "Desc", 100.0, 5)
    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.price = 80.0
    captured = capsys.readouterr()
    assert "Изменение цены отменено" in captured.out
    assert product.price == 100.0


def test_price_setter_increase(monkeypatch):
    """Увеличение цены – не требует подтверждения, цена меняется"""
    product = Product("Test", "Desc", 100.0, 5)
    product.price = 150.0
    assert product.price == 150.0


def test_new_product_no_duplicates():
    """new_product создаёт новый продукт, если нет совпадений по имени"""
    existing = []
    data = {"name": "Phone", "description": "Smart", "price": 500.0, "quantity": 10}
    product = Product.new_product(data, existing)
    assert product.name == "Phone"
    assert product.price == 500.0
    assert product.quantity == 10


def test_new_product_with_duplicate():
    """При дубликате: quantity складывается, price берётся максимальный"""
    existing = [Product("Phone", "Old", 400.0, 5)]
    data = {"name": "Phone", "description": "New", "price": 450.0, "quantity": 3}
    returned_product = Product.new_product(data, existing)
    # Должен вернуть существующий объект
    assert returned_product is existing[0]
    assert existing[0].quantity == 8  # 5 + 3
    assert existing[0].price == 450.0  # max(400,450)


def test_new_product_with_duplicate_lower_price():
    """Дубликат с меньшей ценой – цена не меняется"""
    existing = [Product("Phone", "Old", 500.0, 5)]
    data = {"name": "Phone", "description": "New", "price": 450.0, "quantity": 2}
    Product.new_product(data, existing)
    assert existing[0].price == 500.0
    assert existing[0].quantity == 7


def test_new_product_without_existing_list():
    """Если список existing не передан, всегда создаётся новый продукт"""
    data = {"name": "Gadget", "description": "Thing", "price": 99.0, "quantity": 1}
    product = Product.new_product(data)
    assert product.name == "Gadget"
    # При отсутствии списка дубликаты не проверяются
