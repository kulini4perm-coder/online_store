from src.product import Product


class Category:
    """Класс, представляющий категории товаров."""

    name: str
    description: str
    __products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """Метод для добавления товара в категорию."""

        self.__products.append(product)
        Category.product_count += 1  # При добавлении увеличиваем счетчик

    @property
    def products(self) -> str:
        """Геттер, который возвращает строку со всеми продуктами по шаблону"""

        result = ""
        for product in self.__products:
            # Шаблон: "Название продукта, X руб. Остаток: X шт.\n"
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result
