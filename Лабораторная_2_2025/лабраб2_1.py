class Book:
    def __init__(self, id_, name, pages):
        self.id = id_  # Идентификатор книги
        self.name = name  # Название книги
        self.pages = pages  # Количество страниц в книге

    def __str__(self):
        return f'Книга "{self.name}"'  # Возвращает строку с названием книги

    def __repr__(self):
        return f'Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})'  # Для создания нового экземпляра


# Пример базы данных книг
BOOKS_DATABASE = [
    {"id": 1, "name": "1984", "pages": 328},
    {"id": 2, "name": "Мастер и Маргарита", "pages": 400},
]

if __name__ == '__main__':
    # Инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    for book in list_books:
        print(book)  # Проверяем метод __str__

    print(list_books)  # Проверяем метод __repr__
