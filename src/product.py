from typing import Any, Self

from src.base_product import BaseMixin, BaseProduct


class Product(BaseMixin, BaseProduct):
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
        super().__init__(name, description, price, quantity)

    def __repr__(self) -> str:
        """Реализация repr для корректного отображения состояния объекта."""

        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.__price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> float:
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных типов!")
        return float((self.price * self.quantity) + (other.price * other.quantity))

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
