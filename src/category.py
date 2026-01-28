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

    def __str__(self) -> str:
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        # Проверяем, что добавляемый объект — это Product или его наследник
        if not isinstance(product, Product):
            raise TypeError("Добавлять в категорию можно только товары (Product и его наследники)")

        self.__products.append(product)
        Category.product_count += 1  # При добавлении увеличиваем счетчик

    @property
    def products(self) -> str:
        """Геттер, который возвращает строку со всеми продуктами по шаблону"""

        result = ""
        for product in self.__products:
            # Шаблон теперь прописан в классе Product в методе __str__
            result += str(product) + "\n"
        return result
