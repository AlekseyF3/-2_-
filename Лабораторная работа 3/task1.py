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
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Класс бумажной книги. """

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # вызывает setter с проверкой

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("pages должно быть целым числом")
        if value <= 0:
            raise ValueError("pages должно быть положительным числом")
        self._pages = value

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, "
                f"author={self.author!r}, pages={self.pages})")


class AudioBook(Book):
    """ Класс аудиокниги. """

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # вызывает setter с проверкой

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("duration должно быть числом (float или int)")
        if value <= 0:
            raise ValueError("duration должно быть положительным числом")
        self._duration = float(value)

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, "
                f"author={self.author!r}, duration={self.duration})")
