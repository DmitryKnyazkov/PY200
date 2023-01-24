class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages_):
        # super().__init__(name, author)
        self._name = name
        self._author = author
        self.pages = pages_
        # self.set_pages(pages_)

    def valid(self, pages_):
        if not isinstance(pages_, int):
            raise TypeError

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages_):
        self.valid(pages_)
        self.__pages = pages_

    # def __str__(self):
    #     return f"Книга {self.name}. Автор {self.author}. Станиц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        # super().__init__(name, author)
        self._name = name
        self._author = author
        self.duration = duration
        # self.set_duration(duration)

    # def __str__(self):
    #     return f"Книга {self.name}. Автор {self.author}, Длительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

    def valid(self, duration_):
        if not isinstance(duration_, float):
            raise TypeError

    # def set_duration(self, duration_):
    #     self.valid(duration_)
    #     self.duration = duration_

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.valid(duration)
        self.__duration = duration

if __name__ == "__main__":
    b = Book("Собачье сердце", "Булгагов")
    print(b)
    print(repr(b))
    print()
    p = PaperBook("Война и мир", "Толстой", 1000)
    print(p)
    print(repr(p))
    print()
    a = AudioBook("Муму", "Тургеньев", 100.76)
    print(a)
    print(repr(a))

    a.duration = 12.23
    print(repr(a))

