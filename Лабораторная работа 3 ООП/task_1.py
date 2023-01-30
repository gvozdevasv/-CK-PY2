class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга: {self.name} Автор: {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Дочерний класс """

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа str")

        if pages <= 0:
            raise ValueError("Количество страниц не может быть отрицательным числом")
        self.pages = pages

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}. Количество страниц {self.pages}"


class AudioBook(Book):
    """ Дочерний класс """

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError("Длительность должна быть типа float")

        if duration <= 0:
            raise ValueError("Длительность не может быть отрицательным числом")
        self.duration = duration

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}. Длительность {self.duration}"


print(PaperBook('Роман', 'А.С.Пушкин', 250))
print(AudioBook('Солнечный удар', 'И.А.Бунин', 1.25))
