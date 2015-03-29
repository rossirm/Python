__author__ = 'Боян'


def on_budget(books, budget):
    books_wanted = sorted(books)
    paid = sum(books) - budget
    order = {
        "books_on_budget": 0,
        "loan": max(0, paid)
    }

    for book in books_wanted:
        if book <= budget:
            budget -= book
            order["books_on_budget"] += 1

    return order


print(on_budget([0, 10, 100, 5, 3, 8, 25], 35))
print(on_budget([0, 0, 0], 10))
print(on_budget([50, 60, 10], 20))