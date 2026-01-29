import pytest

from src.category import Category
from src.product import Product
from src.smartphone import Smartphone


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


# def test_category_products_property(category_smartphones: Category) -> None:
# Исключен как дублирующий - создан новый тест test_category_products_output,
# который также проверяет строковый вывод геттера.


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


def test_product_str(product_iphone: Product) -> None:
    # Проверка строкового отображения продукта
    assert str(product_iphone) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_category_str(category_smartphones: Category) -> None:
    # Проверка строкового отображения категории (суммарное кол-во товаров: 8 + 5)
    assert str(category_smartphones) == "Смартфоны, количество продуктов: 13 шт."


def test_products_addition(product_iphone: Product, product_samsung: Product) -> None:
    # Проверка сложения двух продуктов.
    assert product_iphone + product_samsung == 2580000.0


def test_category_products_output(category_smartphones: Category) -> None:
    # Проверка, что геттер продуктов использует новое строковое отображение
    output = category_smartphones.products
    assert "Iphone 15, 210000.0 руб. Остаток: 8 шт." in output
    assert "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт." in output


def test_addition_error(product_iphone: Product) -> None:
    # Проверка ошибки при сложении продукта с чем-то другим
    with pytest.raises(TypeError):
        product_iphone + 10


def test_addition_different_classes(product_iphone: Product, grass_elite: Product) -> None:
    # Проверка, что нельзя сложить смартфон и траву
    with pytest.raises(TypeError):
        product_iphone + grass_elite


def test_add_invalid_product(category_smartphones: Category) -> None:
    # Проверка, что в категорию нельзя добавить не Product
    with pytest.raises(TypeError):
        category_smartphones.add_product("Это не продукт, а строка")  # type: ignore

    with pytest.raises(TypeError):
        category_smartphones.add_product(12345)  # type: ignore


def test_smartphone_specific_attributes(smartphone_iphone_15: Smartphone) -> None:
    # Проверяем, что данные Smartphone не теряются при инициализации
    assert smartphone_iphone_15.model == "15"
    assert smartphone_iphone_15.memory == 512
