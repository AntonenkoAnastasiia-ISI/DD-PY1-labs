
class Vehicle:
    """Базовый класс для транспортных средств."""

    def __init__(self, brand: str, model: str, year: int) -> None:
        """Инициализация транспортного средства.

        param:
            brand (str): Марка транспортного средства.
            model (str): Модель транспортного средства.
            year (int): Год выпуска.
        """
        self.__brand = brand  # Непубличный атрибут
        self.__model = model  # Непубличный атрибут
        self.year = year

    def __str__(self) -> str:
        """Возвращает представление объекта в виде строки."""
        return f"{self.year} {self.__brand} {self.__model}"

    def __repr__(self) -> str:
        """Возвращает формальное представление объекта в виде строки."""
        return f"Vehicle(brand='{self.__brand}', model='{self.__model}', year={self.year})"

    def start_engine(self) -> str:
        """Запускает двигатель транспортного средства.

        Returns:
            str: Сообщение о запуске двигателя.
        """
        return f"The engine of {self} has started."


class Car(Vehicle):
    """Класс для легковых автомобилей."""

    def __init__(self, brand: str, model: str, year: int, doors: int) -> None:
        """Инициализация легкового автомобиля.

        :param
            brand (str): Марка легкового автомобиля.
            model (str): Модель легкового автомобиля.
            year (int): Год выпуска.
            doors (int): Количество дверей.
        """
        super().__init__(brand, model, year)
        self.doors = doors

    def __str__(self) -> str:
        """Возвращает представление легкового автомобиля в виде строки."""
        return f"{super().__str__()} with {self.doors} doors"

    def honk(self) -> str:
        """Издает звук сигнала.

        Returns:
            str: Сообщение о сигнале.
        """
        return f"{self.__brand} {self.__model} says honk!"


class Truck(Vehicle):
    """Класс для грузовых автомобилей."""

    def __init__(self, brand: str, model: str, year: int, capacity: float) -> None:
        """Инициализация грузового автомобиля.

        :param
            brand (str): Марка грузового автомобиля.
            model (str): Модель грузового автомобиля.
            year (int): Год выпуска.
            capacity (float): Грузоподъемность в тоннах.
        """
        super().__init__(brand, model, year)
        self.capacity = capacity

    def __str__(self) -> str:
        """Возвращает представление грузового автомобиля в виде строки."""
        return f"{super().__str__()} with a capacity of {self.capacity} tons"

    def load_cargo(self, weight: float) -> str:
        """Загружает груз в грузовик.

        :param
            weight (float): Вес груза.

        Returns:
            str: Сообщение о загрузке груза.

        Raises:
            ValueError: Если вес груза превышает грузоподъемность.
        """
        if weight > self.capacity:
            raise ValueError("Cannot load cargo: exceeds capacity.")
        return f"Loaded {weight} tons of cargo in {self.__brand} {self.__model}."


class SocialNetwork:
    """Базовый класс для социальных сетей."""

    def __init__(self, name: str, users_count: int) -> None:
        """Инициализация социальной сети.

        :param name: Название социальной сети.
        :param users_count: Количество пользователей.
        """
        self.name = name
        self.users_count = users_count

    def __str__(self) -> str:
        """Возвращает представление социальной сети в виде строки."""
        return f"{self.name} with {self.users_count} users"

    def __repr__(self) -> str:
        """Возвращает формальное представление социальной сети в виде строки."""
        return f"SocialNetwork(name='{self.name}', users_count={self.users_count})"


class VK(SocialNetwork):
    """Класс для социальной сети VK."""

    def __init__(self, users_count: int) -> None:
        """Инициализация социальной сети VK.

        :param users_count: Количество пользователей.
        """
        super().__init__("VK", users_count)

    def post(self, content: str) -> str:
        """Создает пост в VK.

        :param content: Содержимое поста.

        :return: Сообщение о создании поста.
        """
        return f"Posted in VK: {content}"


class Facebook(SocialNetwork):
    """Класс для социальной сети Facebook."""

    def __init__(self, users_count: int) -> None:
        """Инициализация социальной сети Facebook.

        :param users_count: Количество пользователей.
        """
        super().__init__("Facebook", users_count)

    def post(self, content: str) -> str:
        """Создает пост в Facebook.

        :param content: Содержимое поста.

        :return: Сообщение о создании поста.

        Обоснование перегрузки метода:
            Этот метод был перегружен для добавления специфического поведения
            при создании постов в Facebook по сравнению с VK.
        """
        return f"Posted in Facebook: {content}"


# Пример классов Car и Truck
class Car:
    """Класс для автомобилей."""

    def __init__(self, make: str, model: str, year: int, doors: int) -> None:
        """Инициализация автомобиля.

        :param make: Производитель.
        :param model: Модель.
        :param year: Год выпуска.
        :param doors: Количество дверей.
        """
        self.make = make
        self.model = model
        self.year = year
        self.doors = doors

    def start_engine(self) -> str:
        """Запускает двигатель автомобиля."""
        return "Engine started."

    def honk(self) -> str:
        """Сигналит."""
        return "Honk! Honk!"

    def __str__(self) -> str:
        return f"{self.year} {self.make} {self.model} with {self.doors} doors"


class Truck(Car):
    """Класс для грузовиков, наследуется от Car."""

    def __init__(self, make: str, model: str, year: int, cargo_capacity: float) -> None:
        """Инициализация грузовика.

        :param make: Производитель.
        :param model: Модель.
        :param year: Год выпуска.
        :param cargo_capacity: Грузоподъемность.
        """
        super().__init__(make, model, year, doors=2)
        self.cargo_capacity = cargo_capacity

    def load_cargo(self, weight: float) -> str:
        """Загружает груз в грузовик.

        :param weight: Вес груза.

        :return: Сообщение о загрузке груза.
        """
        if weight <= self.cargo_capacity:
            return f"Loaded {weight} tons of cargo."
        else:
            return "Cargo exceeds capacity!"


if __name__ == "__main__":
    # Примеры использования классов
    car = Car("Geely", "Coolray", 2023, 2)
    print(car)
    print(car.start_engine())
    print(car.honk())

    truck = Truck("BMW", "X5", 2019, 18.0)
    print(truck)
    print(truck.load_cargo(15.0))

    vk = VK(40000000)
    print(vk)
    print(vk.post("HI, VK!"))

    facebook = Facebook(1500000000)
    print(facebook)
    print(facebook.post("HI, Facebook!"))


