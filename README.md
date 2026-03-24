# Домашнее задание 14.2

Учебный проект интернет-магазина на Python. Реализованы классы `Product` и `Category` с инкапсуляцией, геттерами/сеттерами, класс-методом и тестами.

## 🚀 Основное

- Класс `Product`: название, описание, цена (приватная с валидацией), количество.
- Класс `Category`: название, описание, приватный список товаров с методом `add_product()`.
- Геттер для списка товаров в категории (форматированный вывод).
- Класс-метод `new_product()` для создания товара из словаря (с проверкой дубликатов по имени).
- Тесты на `pytest`.

## ⚙️ Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/terpi228/hw14.2.git
   cd hw14.2
Установите зависимости через Poetry:

    ```bash
    poetry install
Активируйте окружение:

    ```bash
    poetry shell
Запустите основной скрипт (пример использования):

    ```bash
    python main.py
🧪 Тестирование
Запуск всех тестов:

    ```bash
    pytest
Или через Poetry:

    ```bash
    poetry run pytest
📁 Структура
  ```text
hw14.2/<br>
├── product.py          # Класс Product<br>
├── category.py         # Класс Category<br>
├── main.py             # Пример использования<br>
├── test_product.py     # Тесты Product<br>
├── test_category.py    # Тесты Category<br>
├── pyproject.toml      # Зависимости (Poetry)<br>
├── poetry.lock<br>
└── README.md<br>
👨‍💻 Автор
terpi228
