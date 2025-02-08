class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    """ Свойства с доступом только для чтения. """
    def name(self):
        return self._name

    """ Свойства с доступом только для чтения. """
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        Book.__init__(self, name, author)  # Явный вызов конструктора родительского класса
        self.pages = pages

    """ Свойства с доступом только для чтения. """
    def pages(self):
        return self._pages

    """ набор страниц.  """

    def pages(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Страниц: {self.pages}"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        Book.__init__(self, name, author)  # Явный вызов конструктора родительского класса
        self.duration = duration

    """ Свойства с доступом только для чтения. """
    def duration(self):
        return self._duration

    """ установщик длительности """

    def duration(self, value: float):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = value

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Продолжительность: {self.duration} часов"


# Пример использования
paper_book = PaperBook("1984", "Джордж Оруэлл", 328)
audio_book = AudioBook("Гарри Поттер и философский камень", "Джоан Роулинг", 8.5)

print(paper_book)  # Бумажная книга 1984. Автор Джордж Оруэлл. Страниц: 328
print(audio_book)  # Аудиокнига Гарри Поттер и философский камень. Автор Джоан Роулинг. Продолжительность: 8.5 часов
print(repr(paper_book))  # Book(name='1984', author='Джордж Оруэлл')
print(repr(audio_book))   # Book(name='Гарри Поттер и философский камень', author='Джоан Роулинг')