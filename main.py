from product import Product
from category import Category

product1_data = {'name': 'Ноутбук', 'price': 80000, 'quantity': 5}
product1 = Product.new_product(product1_data)

product2_data = {'name': 'Мышь', 'price': 1500, 'quantity': 20}
product2 = Product.new_product(product2_data)

category = Category("Электроникa")


category.add_product(product1)
category.add_product(product2)

for info in category.get_products_info():
    print(info)