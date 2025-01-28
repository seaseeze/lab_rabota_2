BOOKS_DATABASE = [
    {"id": 1, "name": "1984", "pages": 328},
    {"id": 2, "name": "Мастер и Маргарита", "pages": 400},
]


# TODO написать класс Book
class Book:
    def __init__(self, book_id, name, author):
        self.id = book_id
        self.name = name
        self.author = author

    def __repr__(self):
        return f"Book(id={self.id}, name='{self.name}', author='{self.author}')"

# TODO написать класс Librar

class Library:
    def __init__(self, books=None):
        self.books = books if books is not None else []

    def get_next_book_id(self):
        if not self.books:
            return 1
        else:
            return max(book.id for book in self.books) + 1

    def get_index_by_book_id(self, book_id):
        for idx, book in enumerate(self.books):
            if book.id == book_id:
                return idx
        raise ValueError("Книги с запрашиваемым id не существует")


# Пример использования
if __name__ == "__main__":
    library = Library()

    print("Следующий ID для книги:", library.get_next_book_id())  # Ожидается 1

    # Добавляем книгу
    book_1984 = Book(library.get_next_book_id(), "1984", "Джордж Оруэлл")
    library.books.append(book_1984)

    print("Следующий ID для книги:", library.get_next_book_id())  # Ожидается 2

    try:
        index = library.get_index_by_book_id(1)  # Ожидается 0
        print("Индекс книги с id 1:", index)
    except ValueError as e:
        print(e)

    try:
        index = library.get_index_by_book_id(2)  # Ожидается ошибка
        print("Индекс книги с id 2:", index)
    except ValueError as e:
        print(e)

# новая строка ниже этого комментария
