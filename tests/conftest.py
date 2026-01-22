import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_iphone() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_samsung() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый", 180000.0, 5)


@pytest.fixture
def category_smartphones(product_iphone: Product, product_samsung: Product) -> Category:
    # Сбрасываем счетчики перед тестом, чтобы тесты были независимыми
    Category.category_count = 0
    Category.product_count = 0
    return Category("Смартфоны", "Описание категории", [product_iphone, product_samsung])
