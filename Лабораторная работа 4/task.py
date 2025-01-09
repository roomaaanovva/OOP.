from abc import ABC, abstractmethod
import math


class GeometricFigure:
    """
    Базовый класс для геометрических фигур.
    """

    def __init__(self, name: str) -> None:
        """
        Конструктор базового класса.

        :param name: Название фигуры.
        """
        self._name = name  # Инкапсуляция: название фигуры доступно только внутри класса

    def __str__(self) -> str:
        """
        Возвращает строковое представление фигуры.
        """
        return f"Фигура: {self._name}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление фигуры для разработчика.
        """
        return f"GeometricFigure(name='{self._name}')"

    @abstractmethod
    def area(self) -> float:
        """
        Абстрактный метод для вычисления площади фигуры.
        """
        pass


class Circle(GeometricFigure):
    """
    Класс для круга.
    """

    def __init__(self, name: str, radius: float) -> None:
        """
        Конструктор круга.

        :param name: Название круга.
        :param radius: Радиус круга.
        """
        super().__init__(name)
        self._radius = radius  # Инкапсуляция: радиус доступен только внутри класса

    def __str__(self) -> str:
        """
        Перегруженный метод для строкового представления круга.
        """
        return f"Круг '{self._name}', радиус: {self._radius}"

    def __repr__(self) -> str:
        """
        Перегруженный метод для строкового представления круга для разработчика.
        """
        return f"Circle(name='{self._name}', radius={self._radius})"

    def area(self) -> float:
        """
        Вычисление площади круга.
        """
        return math.pi * self._radius ** 2

    def perimeter(self) -> float:
        """
        Вычисление периметра круга.
        """
        return 2 * math.pi * self._radius

    def scale(self, factor: float) -> None:
        """
        Изменение размера круга на заданный множитель.

        :param factor: Множитель изменения размера.
        """
        self._radius *= factor
