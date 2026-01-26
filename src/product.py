from typing import Any, Self


class Product:
    """Класс, представляющий товары."""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> float:
        if isinstance(other, Product):
            # (Цена1 * Кол-во1) + (Цена2 * Кол-во2)
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError("Складывать можно только объекты класса Product")

    @classmethod
    def new_product(cls, product_data: dict) -> Self:
        """Класс-метод для создания объекта Product из словаря."""

        return cls(product_data["name"], product_data["description"], product_data["price"], product_data["quantity"])

    @property
    def price(self) -> float:
        """Геттер для атрибута цены."""

        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для атрибута цены с проверкой корректности."""

        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value
