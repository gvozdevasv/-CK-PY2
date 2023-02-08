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
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_page: int) -> None:
        if not isinstance(new_page, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_page <= 0:
            raise ValueError("Количество страниц не может быть отрицательным числом")
        self._pages = new_page

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}. Количество страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ Дочерний класс """

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Длительность должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Длительность не может быть отрицательным числом")
        self._duration = new_duration

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}. Длительность: {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


print(PaperBook('Роман', 'А.С.Пушкин', 250))
print(AudioBook('Солнечный удар', 'И.А.Бунин', 1.25))
