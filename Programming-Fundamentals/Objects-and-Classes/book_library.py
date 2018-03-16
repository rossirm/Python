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

    def sort_books(self):
        authors = {}
        for book in self.book_list:
            if book.author not in authors:
                authors[book.author] = book.price
            else:
                authors[book.author] += book.price

        result = ''
        for author, total in sorted(authors.items(), key=lambda x: (-x[1], x[0])):
            result += f'{author} -> {total:.2f}\n'
        return result


count = int(input())
collection = []
for b in range(count):
    collection.append(Book.read_book())

my_collection = Library(collection)
print(my_collection.sort_books())
