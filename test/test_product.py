import pytest
from src.product import BaseProduct, Product, Smartphone, LawnGrass


def test_base_product_abstract():
    """Проверяем, что BaseProduct нельзя создать."""
    with pytest.raises(TypeError):
        BaseProduct()


def test_log_mixin(capsys):
    """Проверяем, что при создании объекта выводится лог."""
    p = Product("Телефон", 50000, 10)
    captured = capsys.readouterr()
    # В выводе должно быть сообщение от миксина
    assert "Создан объект класса Product('Телефон', 50000, 10)" in captured.out

    s = Smartphone("iPhone", 120000, 1, "A16", "15", 128, "черный")
    captured = capsys.readouterr()
    assert "Создан объект класса Smartphone('iPhone', 120000, 1, 'A16', '15', 128, 'черный')" in captured.out