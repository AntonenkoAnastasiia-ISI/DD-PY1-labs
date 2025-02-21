# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from abc import ABC, abstractmethod

class Chairs:
    """Класс, описывающий стул."""
    def __init__(self, weight: float, volume: float, material: str):
        """
               Инициализация атрибутов стула.

               :param weight: Вес стола (должен быть положительным).
               :param volume: Объем стола (должен быть положительным).
               :param material: Материал стола.

                :raises ValueError: Если weight не положительный.
                :raises ValueError: Если volume не положительный.
                :raises ValueError: Если material пустой.
               """
        if not isinstance(weight,(int, float)):
            raise TypeError
        if weight <= 0:
            raise ValueError("Вес должен быть положительным.")
        self.weight = weight

        if not isinstance(material, (str)):
            raise TypeError
        if not material:
            raise ValueError("Материал не может быть пустым.")
        self.material = material

        if not isinstance(volume,(int, float)):
            raise TypeError
        if volume <=0:
            raise ValueError("Объем должен быть положительным.")
        self.volume = volume

    def calculate_density(self) -> float:
            """Расчет плотности стула."""
            return self.weight / self.volume

    def describe(self) -> str:
        """Описание стола."""
        return f"Стул из {self.material}, вес: {self.weight} кг, объем: {self.volume} м³."



class Tree:
    """Класс, описывающий дерево."""
    def __init__(self, species: str, age: int) -> None:
        """
                       Инициализация атрибутов стула.

                       :param species: Вид дерева.
                       :param age: Возраст дерева (должен быть положительным и целым).

                        :raises ValueError: Если age не положительный.
                        :raises ValueError: Если species пустой.
                       """
        if not isinstance(species, str) or not species:
            raise ValueError("Вид дерева должен быть непустой строкой.")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст дерева должен быть неотрицательным целым числом.")

        self.species = species
        self.age = age

    def grow(self) -> None:
        """
        Дерево растет.

        :return: None

        """
        ...

    def shed_leaves(self) -> None:
        """
        Дерево сбрасывает листья.

        :return: None

        """
        ...

    def describe(self) -> str:
        """Описание дерева."""
        return f"{self.species}, возраст: {self.age} лет."


class Furniture(ABC):
    """Класс, описывающий мебель."""
    def __init__(self, material: str, color: str) -> None:
        """
                               Инициализация атрибутов стула.

                               :param material: Материал мебели.
                               :param color: Цвет мебели.

                                :raises ValueError: Если material пустой.
                                :raises ValueError: Если color пустой.
                               """
        if not isinstance(material, str) or not material:
            raise ValueError("Материал должен быть непустой строкой.")

        if not isinstance(color, str) or not color:
            raise ValueError("Цвет должен быть непустой строкой.")

        self.material = material
        self.color = color

    def use(self) -> None:
        """
        Использовать мебель.

        :return: None

        """
        ...

    def clean(self) -> None:
        """
        Убрать мебель.

        :return: None

        """
        ...

    def describe(self) -> str:
        """Описание мебели."""
        return f"материал: {self.material}, цвет: {self.color}."


if __name__ == "__main__":
    doctest.testmod()
    chair = Chairs(7, 0.5, "пластик")
    print(chair.describe())
    tree = Tree("дуб", 5)
    print(tree.describe())
    cupboard = Furniture("дерево", "черный")
    print(cupboard.describe())
    # Запуск doctest для проверки работы методов
    result = doctest.testmod()
    # Вывод результата тестирования
    print(result)

...

