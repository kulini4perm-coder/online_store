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
    assert len(category_smartphones.products) == 2


def test_category_counts(category_smartphones: Category) -> None:
    # Тест подсчета количества категорий и продуктов
    #  Добавляем одну категорию
    p3 = Product("Xiaomi", "Note 11", 31000.0, 14)
    Category("Телевизоры", "Техника", [p3])

    assert Category.category_count == 2
    assert Category.product_count == 3


def test_product_in_category(category_smartphones: Category) -> None:
    # Тест, что в списке товаров действительно лежат объекты Product
    assert isinstance(category_smartphones.products[0], Product)
    assert category_smartphones.products[0].name == "Iphone 15"
