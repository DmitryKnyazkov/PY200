class Book:

    def __init__(self, id, name, pages, next_book=None):
        self.id = id
        self.name = name
        self.pages = pages
        self.next_book = next_book
        self.set_next(next_book)

    def __str__(self):
        return f'Книга {self.name}'

    def __repr__(self):
        return f'Book(id={self.id!r}, name={self.name!r}, pages={self.pages!r})'

    def is_valid(self, node) -> None:
        if not isinstance(node, (None | Book)):
            raise TypeError

    def set_next(self, next_) -> None:
        self.is_valid(next_)
        self.next_book = next_


class Library:
    def __init__(self, books=[]):
        self.books = books

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        else:
            return f'Следующий id книги должен быть - {len(self.books) + 1}'

    def get_index_by_book_id(self, index):
        for i,book_ in enumerate(self.books):
            if book_.id == index:
                return f'Индекс книги в списке {i}'
        raise ValueError("Книги с запрашиваемым id не существует")

    def __repr__(self):
        return f"{self.books}"

    def append(self, new_book: Book):
        """ Добавление элемента в конец связного списка. """
        self.books.append(new_book)


if __name__ == "__main__":
    a = Book(1, "aaa", 5)
    b = Book(2,'sss', 10)
    bb = Library()
    print(bb)
    bb.append(a)
    print(bb)
    bb.append(b)
    print(bb)
    print(bb.get_next_book_id())
    print(bb.get_index_by_book_id(2))
    c = Book(3, 'ddd', 20)
    bb.append(c)
    print(bb)