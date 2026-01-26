import pytest

from src.category import Category
from src.product import Product


def test_product_init(product_iphone: Product) -> None:
    # Тестируем правильную инициализацию объекта Product
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512GB, Gray space"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8


def test_category_init(category_smartphones: Category) -> None:
    # Тестируем правильную инициализацию объекта Category
    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.description == "Описание категории"
    assert len(category_smartphones._Category__products) == 2  # type: ignore


def test_category_counts(category_smartphones: Category) -> None:
    # Тест подсчета количества категорий и продуктов
    #  Добавляем одну категорию
    p3 = Product("Xiaomi", "Note 11", 31000.0, 14)
    Category("Телевизоры", "Техника", [p3])

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_category_products_property(category_smartphones: Category) -> None:
    """Тест геттера products, который возвращает строку со всеми продуктами."""
    # Важно: \n должен быть в конце каждой строки, включая последнюю
    expected_output = (
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n" "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
    )
    assert category_smartphones.products == expected_output


def test_add_product(category_smartphones: Category) -> None:
    # Тест метода add_product
    new_product = Product("Xiaomi", "Note 11", 30000.0, 10)
    category_smartphones.add_product(new_product)
    assert Category.product_count == 3
    assert "Xiaomi" in category_smartphones.products


def test_new_product_classmethod() -> None:
    # Тест метода new_product
    data = {"name": "Test", "description": "Test", "price": 100.0, "quantity": 1}
    product = Product.new_product(data)
    assert product.name == "Test"
    assert product.price == 100.0


def test_price_setter(product_iphone: Product, capsys: pytest.CaptureFixture[str]) -> None:
    # Тест сеттера цены с проверкой <= 0
    product_iphone.price = 250000.0
    assert product_iphone.price == 250000.0

    product_iphone.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product_iphone.price == 250000.0  # Цена не изменилась
