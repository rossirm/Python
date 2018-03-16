from datetime import date


class Book:
    def __init__(self, title, author, publisher, release_date, isbn, price):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.release_date = release_date
        self.isbn = isbn
        self.price = price

    @staticmethod
    def read_book():
        title, author, publisher, release_date, isbn, price = input().split(' ')
        day, month, year = list(map(int, release_date.split('.')))
        release_date = date(year=year, month=month, day=day)
        price = float(price)
        return Book(title, author, publisher, release_date, isbn, price)


class Library:
    def __init__(self, book_list):
        self.book_list = book_list

    def sort_books(self, some_date):
        books = {}
        filtered_books = [book for book in self.book_list if book.release_date > some_date]
        for book in filtered_books:
            if book.title not in books:
                books[book.title] = book.release_date
            else:
                books[book.title] += book.release_date

        result = ''
        for name, r_date in sorted(books.items(), key=lambda x: (x[1], x[0])):
            f_date = r_date.strftime("%d.%m.%Y")
            result += f'{name} -> {f_date}\n'
        return result


count = int(input())
collection = []
for b in range(count):
    collection.append(Book.read_book())

d, m, y = list(map(int, input().split('.')))
issue_date = date(year=y, month=m, day=d)

my_collection = Library(collection)
print(my_collection.sort_books(issue_date))
