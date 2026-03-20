
import pytest
from product import Product, Smartphone, LawnGrass


def test_product_str():
    p = Product("Смартфон", 40000, 3)
    assert str(p) == "Смартфон, 40000 руб. Остаток: 3 шт."

def test_product_add():
    p1 = Product("Ноутбук", 80000, 2)
    p2 = Product("Мышь", 1500, 5)
    total_cost = p1 + p2
    expected = 80000 * 2 + 1500 * 5
    assert total_cost == expected

def test_product_add_wrong_type():
    p1 = Product("Книга", 500, 10)
    with pytest.raises(TypeError):
        p1 + "не товар"

def test_smartphone_creation():
    phone = Smartphone("iPhone 15", 120000, 5, "A16 Bionic", "15 Pro", 256, "черный")
    assert phone.name == "iPhone 15"
    assert phone.price == 120000
    assert phone.quantity == 5
    assert phone.efficiency == "A16 Bionic"
    assert phone.model == "15 Pro"
    assert phone.memory == 256
    assert phone.color == "черный"

def test_lawn_grass_creation():
    grass = LawnGrass("Газонная трава", 1500, 100, "Россия", "7-10 дней", "зеленый")
    assert grass.name == "Газонная трава"
    assert grass.price == 1500
    assert grass.quantity == 100
    assert grass.country == "Россия"
    assert grass.germination_period == "7-10 дней"
    assert grass.color == "зеленый"

def test_product_add_same_type():
    p1 = Product("Ноутбук", 80000, 2)
    p2 = Product("Мышь", 1500, 5)
    assert (p1 + p2) == 80000*2 + 1500*5

def test_product_add_different_types():
    phone = Smartphone("iPhone", 120000, 1, "A16", "15", 128, "черный")
    grass = LawnGrass("Трава", 1000, 10, "РФ", "10 дней", "зеленый")
    with pytest.raises(TypeError):
        phone + grass

def test_product_add_smartphone_with_self():
    phone1 = Smartphone("iPhone", 120000, 1, "A16", "15", 128, "черный")
    phone2 = Smartphone("Samsung", 90000, 2, "Exynos", "S23", 256, "белый")
    assert (phone1 + phone2) == 120000*1 + 90000*2

def test_product_add_lawn_with_self():
    grass1 = LawnGrass("Трава1", 1000, 10, "РФ", "10 дней", "зеленый")
    grass2 = LawnGrass("Трава2", 1500, 5, "США", "14 дней", "темно-зеленый")
    assert (grass1 + grass2) == 1000*10 + 1500*5