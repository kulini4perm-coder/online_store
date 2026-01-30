from abc import ABC, abstractmethod
from typing import Any, Self


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: dict) -> Self:
        pass


class BaseMixin:
    """Миксин для логирования создания объекта."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        # Печатаем информацию о созданном объекте
        print(f"{self.__class__.__name__}({', '.join([repr(a) for a in args])})")
        super().__init__(*args, **kwargs)
